from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="rotten_tomatoes_cli",
    description="Rotten Tomatoes Command Line Tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Jae Bradley",
    author_email="jae.b.bradley@gmail.com",
    url="https://github.com/jaebradley/rotten_tomatoes_cli",
    version="0.0.3",
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    python_requires=">=3.4",
    install_requires=[
        "Click==6.7",
        "rotten_tomatoes_client==0.0.3",
        "terminaltables==3.1.0",
        "termcolor==1.1.0"
    ],
    entry_points={
        "console_scripts": [
            "rotten= scripts.rotten:rotten"
        ],
    },
    keywords=[
        "Movies",
        "Rotten Tomatoes",
    ],
    classifiers=[]
)