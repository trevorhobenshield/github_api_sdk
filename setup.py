from pathlib import Path
from textwrap import dedent

from setuptools import find_packages, setup

install_requires = [
    "nest-asyncio",
    # 'uvloop; platform_system != "Windows"',
    "httpx[http2]",
    "pydantic>=1.9.0, <3",
    "typing-extensions>=4.10, <5",
    "anyio>=3.5.0, <5",
    "distro>=1.7.0, <2",
    "sniffio",
]

about = {}
exec((Path().cwd() / "github_api_sdk" / "_version.py").read_text(), about)

setup(
    name=about["__title__"],
    version=about["__version__"],
    author=about["__author__"],
    description=about["__description__"],
    license=about["__license__"],
    long_description=dedent((Path().cwd() / "README.md").read_text()),
    python_requires=">=3.12.10",
    long_description_content_type="text/markdown",
    author_email="trevorhobenshield@gmail.com",
    url="https://github.com/trevorhobenshield/github_api_client",
    install_requires=install_requires,
    keywords="fluent github api client",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
