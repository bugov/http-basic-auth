from os.path import abspath, dirname, join, normpath

from setuptools import setup

from http_basic_auth import __version__

requires = []

setup(
    # Basic package information:
    name='http-basic-auth',
    version=__version__,
    py_modules=('http_basic_auth',),

    # Packaging options:
    zip_safe=False,
    include_package_data=True,

    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    # Package dependencies:
    requires=requires,
    tests_require=requires + ["pytest"],
    setup_requires=requires + ["pytest-runner"],
    install_requires=requires,

    # Metadata for PyPI:
    author='Georgy Bazhukov',
    author_email='georgy.bazhukov@gmail.com',
    license='BSD',
    url='https://github.com/bugov/http-basic-auth',
    keywords='security basic auth http',
    description='HTTP Basic Auth implementation',
    long_description=open(
        normpath(join(dirname(abspath(__file__)), 'README.md')), encoding='utf-8'
    ).read()
)
