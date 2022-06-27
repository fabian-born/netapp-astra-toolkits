import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as req:
    all_reqs = req.read().split("\n")


setuptools.setup(
    name="pyastractl",
    version="2.1.1",
    py_modules=["toolkit", "astraSDK"],
    author="Michael Haigh",
    author_email="Michael.Haigh@netapp.com",
    description="Toolkit and SDK for interacting with Astra Control",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NetApp/netapp-astra-toolkits",
    packages=setuptools.find_packages(),
    install_requires=all_reqs,
    entry_points={
        "console_scripts": [
            "pyastractl=toolkit:main",
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)
