from setuptools import setup, find_packages

long_description = open("README.rst").read()

setup(
    name="StackAPI",
    description="Library for interacting with the Stack Exchange API",
    long_description=long_description,
    url="https://github.com/AWegnerGitHub/StackAPI",
    author="Andrew Wegner",
    author_email="pypi@andrewwegner.com",
    maintainer="Andrew Wegner",
    maintainer_email="pypi@andrewwegner.com",
    license="MIT",
    keywords="stackexchange",
    packages=find_packages(exclude=["contrib", "docs", "tests*", "test"]),
    version="0.3.0",
    install_requires=["requests", "six"],
    tests_require=["mock"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    test_suite="tests",
)
