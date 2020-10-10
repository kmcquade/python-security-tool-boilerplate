#!/usr/bin/env python
from invoke import task, Collection, UnexpectedExit, Failure

# Create the necessary collections (namespaces)
ns = Collection()
build = Collection("build")
ns.add_collection(build)


# Build
@task
def build_package(c):
    """Build the package from the current directory contents for use with PyPi"""
    c.run("python -m pip install --upgrade setuptools wheel")
    c.run("python setup.py -q sdist bdist_wheel")


@task(pre=[build_package])
def install_package(c):
    """Install the package built from the current directory contents (not PyPi)"""
    c.run("pip3 install -q dist/*-*.tar.gz")


build.add_task(build_package, "build-package")
build.add_task(install_package, "install-package")
