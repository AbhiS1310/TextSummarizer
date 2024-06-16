from setuptools import setup,find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name = 'textSummarizer',
    version = '1.0.0',
    author = 'abhi',
    description="A small python package for NLP app",
    long_description=long_description,
    long_description_content="text/markdown",
    package_dir= {"": "src"},
    packages = find_packages(where='src')
)