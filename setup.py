from setuptools import setup

setup(
    name='wrecking-check',
    version='0.1.0',
    description='Check your [w]req(uirements).in',
    author='David Szotten',
    url='http://github.com/davidszotten/wrecking_check',
    py_modules=['wrecking_check'],
    entry_points={
        'console_scripts': [
            'wrecking-check=wrecking_check:main',
        ],
    },
    zip_safe=True,
    license='Apache License, Version 2.0',
    classifiers=[
        "Programming Language :: Python",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Intended Audience :: Developers",
    ]
)
