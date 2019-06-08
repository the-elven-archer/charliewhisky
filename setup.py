import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="charliewhisky",
    version="0.1",
    author="Santiago Buczak",
    author_email="the.elven.archer@gmail.com",
    description="Morse encoder and plyaer for python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/the-elven-archer/charliewhisky.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Linux",
    ],
)
