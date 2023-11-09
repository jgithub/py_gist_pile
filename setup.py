from setuptools import setup


REQUIRED_PACKAGES = [
]

__version__ = v0.0.2


setup(
    name="fh_timezone",
    version=__version__,
    description="Kinda like ts-gist-pile, but for python",
    url="https://github.com/jgithub/py-gist-pile",
    author="jgithub",
    python_requires='>=3.10,<4',
    install_requires=REQUIRED_PACKAGES,
    tests_require=REQUIRED_PACKAGES,
    include_package_data=False,
)

