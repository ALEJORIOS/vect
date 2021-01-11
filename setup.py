from setuptools import setup

with open("README.md", "r") as readme_file:
    readme = readme_file.read()
    
setup(

    name = "vect",
    version = "0.0.5b",
    description = "This powerful tool can help you in vector related work in python",
    author = "Alejandro Ríos",
    long_description = readme,
    url = "https://github.com/ALEJORIOS/vect.git",
    keywords = ["vect", "vector", "algebra"],
    packages = ["vect","vect"],
)