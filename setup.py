import os

from setuptools import setup

requires = []


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname), encoding='utf-8').read()


setup(
    # Basic package information:
    name='http-basic-auth',
    version='1.1.3',
    py_modules=('http_basic_auth',),

    # Packaging options:
    zip_safe=False,
    include_package_data=True,
    packages=('http_basic_auth',),

    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
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
    long_description=read('readme.md'),
)
