"""
Packaging information and tools.
"""


from os.path import abspath, dirname, join, normpath

from setuptools import find_packages, setup


setup(
    # Basic package information:
    name="okta-flask-example",
    version="1.0.0",
    packages=find_packages(),
    # Packaging options:
    zip_safe=False,
    include_package_data=True,
    # Package dependencies:
    install_requires=["Flask>=1.0.0", "flask-oidc>=1.4.0", "okta==0.0.4"],
    # Metadata for PyPI:
    author="Randall Degges",
    author_email="r@rdegges.com",
    license="UNLICENSE",
    url="https://github.com/rdegges/okta-flask-example",
    keywords="python security authentication user login registration flask web okta openid connect",
    description="A simple Flask app with user registration and login.",
    long_description=open(
        normpath(join(dirname(abspath(__file__)), "README.rst"))
    ).read(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: Public Domain",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Internet",
    ],
)
