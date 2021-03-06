"""
Setup Documentation
"""
import setuptools 

REQUIRED = [
    "numpy",
    "pandas"
    "matplotlib"
    "sklearn"
]
with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()
    setuptools.setup(
    name="lambdata-bmulas1535_a",
    version = "0.1.2",
    author = "bmulas1535_a",
    description = "A Collection of Data Science Helper Functions",
    long_description = LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://lambdaschool.com/courses/data-science",
    packages=setuptools.find_packages(),
    python_requires=">=3.5",
    install_requires = REQUIRED,
    classifiers=["Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    ]
    )