from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

with open('requirements_dev.txt') as f:
    required_dev = f.read().splitlines()

setup(
    name="mymodule",
    version="0.1",
    packages=find_packages(),
    install_requires=required,
    extras_require={'dev': required_dev},
)
