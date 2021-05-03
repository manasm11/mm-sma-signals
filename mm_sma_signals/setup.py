from setuptools import setup, find_packages

setup(
    name="mm-sma-signals",
    author="Manas Mishra",
    author_email="manas.m22@gmail.com",
    description="Package to give trading signals from list of timestamps and prices",
    long_description=open("../README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/manasm11/mm-sma-signals",
    version="0.0.0",
    packages=find_packages(),
    install_requires=open("requirements.txt").readlines(),
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
)
