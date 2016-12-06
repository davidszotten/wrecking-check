Wrecking check
==============

Check your [w]req(uirements).in

For use in conjunction with `pip-tools <https://github.com/nvie/pip-tools>`_.

Tries to find packages that are no longer top-level requirements. o


Usage
-----

Point at your ``requirements.in`` and top level directory::

    $ wrecking-check requirements.in src/

    foo
    bar


Known limitations
-----------------

Some libraries are required but not directly imported by your code, e.g. pytest
plugins, web servers and django database drivers.


Warning
-------

These are heuristics. Use carefully and at your own risk.
