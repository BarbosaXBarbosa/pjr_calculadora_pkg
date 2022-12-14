from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="pjr_calculadora",
    version="0.0.2",
    author="BarbosaXBarbosa",
    author_email="asobrab123@hotmail.com",
    description="Uma calculadora feita em python com funções para quem quiser usar.",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BarbosaXBarbosa/pjr_calculadora_pkg",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
    setup_requires=['wheel'],
)
