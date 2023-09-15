from setuptools import setup, find_packages

setup(
    name = "diditend",
    packages = find_packages(),
    install_requires = [
        'requests'
        ],
    entry_points = {
        "console_scripts": ['diditend=diditend.runner:main']
        },
    version = "0.0.2",
    description = "Command line utility to notify me (or you) when a process has finished on command line.",
    long_description = "Command line utility to notify me (or you) when a process has finished on command line.",
    author = "marcocspc",
    author_email = "marcocspc@hotmail.com",
    url = "https://github.com/marcocspc/diditend",
)
