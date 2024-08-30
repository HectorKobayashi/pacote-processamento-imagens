from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="basic_math_operations_simple_package",
    version="0.0.1",
    author="hector_kobayashi",
    author_email="hector.kobayashi@gmail.com",
    description="My first Python package, a simple python package with basic operations",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/HectorKobayashi/simple-math-package",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.12',
)