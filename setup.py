import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="trackRetriever",
    version="1.0.1",
    author="Pradhit Gosula",
    author_email="pradhitg@gmail.com",
    description="A package to get the track id's/names of your songs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gosulap/trackRetriever",
    packages=setuptools.find_packages(),
    install_requires = ["spotipy"], 
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)