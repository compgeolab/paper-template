"""
Build and install the code.

Uses versioneer to manage version numbers using git tags.
"""
from setuptools import setup, find_packages

import versioneer


NAME = "{{ cookiecutter.project_slug }}"
LICENSE = "BSD License"
URL = "https://github.com/{{ cookiecutter.gh_repo }}"
VERSION = versioneer.get_version()
CMDCLASS = versioneer.get_cmdclass()
PLATFORMS = "Any"
PACKAGES = find_packages(exclude=["doc"])
SCRIPTS = []
PACKAGE_DATA = {}
with open("requirements.txt") as f:
    INSTALL_REQUIRES = f.readlines()
PYTHON_REQUIRES = ">={{ cookiecutter.python_version }}"

if __name__ == "__main__":
    setup(
        name=NAME,
        version=VERSION,
        license=LICENSE,
        url=URL,
        platforms=PLATFORMS,
        scripts=SCRIPTS,
        packages=PACKAGES,
        package_data=PACKAGE_DATA,
        install_requires=INSTALL_REQUIRES,
        python_requires=PYTHON_REQUIRES,
        cmdclass=CMDCLASS,
    )
