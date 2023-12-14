# type: ignore[no-untyped-call]
"""Setup script for the ShipNeT package."""

import versioneer
from setuptools import find_packages, setup

# Requirements definitions
SETUP_REQUIRES = [
    "setuptools",
]

INSTALL_REQUIRES = [
    "matplotlib",
    "numpy",
    "tqdm",
]

EXTRAS_REQUIRE = {
    "develop": [
        "black",
        "isort",
        "flake8",
        "autopep8",
        "pre-commit",
        "versioneer",
    ],
    "torch": [
        "torch",
        "torch-geometric",
        "pytorch-lightning",
    ],
}

# https://pypi.org/classifiers/
CLASSIFIERS = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "Programming Language :: Python :: 3.11",
    "Environment :: CPU",
    "Topic :: Scientific/Engineering",
    "Topic :: Software Development",
    "Topic :: Software Development :: Libraries",
    "Topic :: Software Development :: Libraries :: Python Modules",
]

setup(
    name="stocknet",
    version=versioneer.get_version(),
    description=("stocknet"),
    license="MIT License",
    author="The stocknet development team",
    url="https://github.com/soeren97/StockNet",
    cmdclass=versioneer.get_cmdclass(),
    packages=find_packages(where="source"),
    package_dir={"": "source"},
    setup_requires=SETUP_REQUIRES,
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRAS_REQUIRE,
    classifiers=CLASSIFIERS,
)
