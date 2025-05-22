from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.rst").read_text()

setup(
    name="django_cityloc_pkg_beebojones",
    version="0.0.1",
    description="A Django app about city locations",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    author="Beebo Jones",
    author_email="your_email@example.com",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["Django>=3.2"],
    python_requires=">=3.8",
)
