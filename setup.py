from setuptools import setup, find_packages

long_description = open('README.rst').read()

setup(
    name='StackAPI',
    description='Library for interacting with the Stack Exchange API',
    long_description=long_description,
    url='https://github.com/AWegnerGitHub/StackAPI',
    author='Andrew Wegner',
    author_email='pypi@andrewwegner.com',
    maintainer='Andrew Wegner',
    maintainer_email='pypi@andrewwegner.com',
    license='MIT',
    keywords='stackexchange',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*', 'test']),
    version='0.1.9',
    install_requires=['requests'],
    tests_require=['mock'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    test_suite='tests'
)
