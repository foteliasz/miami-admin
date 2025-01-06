from setuptools import setup, find_packages

setup(
    name="miami_admin",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    author="foteliasz",
    author_email="foteliasz@dont_spam_me.whatever",
    description="A simple python wrapper for IAM related administrative tools.",
    license="MIT",
    long_description=open("../README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/foteliasz/miami-admin",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.12',
)