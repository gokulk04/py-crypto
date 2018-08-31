import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="py-crypto",
    version="0.0.1",
    author="Gokul Kumarresen",
    author_email="gokul.kumarresen@outlook.com",
    description="A cryptocurrency trading library for Python with current support for Binance and Bittrex.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gokulk04/py-crypto",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)