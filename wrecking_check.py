import ast
import os
import os.path
import sys

from pip._internal.req.req_file import parse_requirements
import pkg_resources
import toml


def read_requirements(filename):
    names = [
       req.req.name
       for req in parse_requirements(filename, session='dummy')
    ]
    return names


def read_pyproject(filename):
    with open(filename) as handle:
        pyproject = toml.load(handle)
    names = [
        name for name in pyproject['tool']['poetry']['dependencies']
        if name != 'python'
    ]
    return names


def name_module_map(req_file):
    if req_file.endswith('.toml'):
        req_names = read_pyproject(req_file)
    else:
        req_names = read_requirements(req_file)

    module_names = [
        list(
            pkg_resources.get_distribution(name)._get_metadata('top_level.txt')
        )
        for name in req_names
    ]

    return zip(req_names, module_names)


def find_py_files(paths):
    for path in paths:
        for dir_path, _, filenames in os.walk(path):
            for filename in filenames:
                if filename.endswith('.py'):
                    yield os.path.join(dir_path, filename)


class Visitor(ast.NodeVisitor):
    def __init__(self):
        self._modules = set()

    def _collect(self, name):
        if name is None:
            return  # "from . import"

        if '.' in name:
            (top_level, _) = name.split('.', 1)
        else:
            top_level = name
        self._modules.add(top_level)

    def generic_visit(self, node):
        if isinstance(node, ast.Import):
            for alias in node.names:
                self._collect(alias.name)

        if isinstance(node, ast.ImportFrom):
            self._collect(node.module)

        super(Visitor, self).generic_visit(node)


def main():
    if len(sys.argv) < 3:
        print("Usage: wrecking-check <requirements file> <path> [<path>, ...]")
        sys.exit(1)

    req_file = sys.argv[1]
    paths = sys.argv[2:]

    visitor = Visitor()
    filenames = find_py_files(paths)
    for filename in filenames:
        with open(filename) as handle:
            source = handle.read()

        module = ast.parse(source)
        visitor.visit(module)

    name_map = name_module_map(req_file)
    for requirement_name, modules in name_map:
        if not any(module in visitor._modules for module in modules):
            print(requirement_name)


if __name__ == '__main__':
    main()
