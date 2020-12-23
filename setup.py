import setuptools

with open("./README.md", "r") as file:
    long_description = file.read()

setuptools.setup(
    name="httpdogs",
    version="1.0.0",
    author="itsmewulf",
    author_email="wulf.developer@gmail.com",
    description="Bringing you closer to your favorite HTTP Dogs.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/itsmewulf/httpdogs",
    keywords="dog, http, request, api, wrapper",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'
)