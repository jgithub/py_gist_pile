from setuptools import setup, find_packages

REQUIRED_PACKAGES = []

__version__ = "v0.0.20"


setup(
    name="py_gist_pile",
    version=__version__,
    description="Kinda like ts-gist-pile, but for python",
    url="https://github.com/jgithub/py_gist_pile",
    author="jgithub",
    python_requires=">=3.10,<4",
    install_requires=REQUIRED_PACKAGES,
    tests_require=REQUIRED_PACKAGES,
    include_package_data=False,
)
