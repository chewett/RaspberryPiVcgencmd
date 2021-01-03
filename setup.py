from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='RaspberryPiVcgencmd',
    version='0.2',
    packages=['RaspberryPiVcgencmd'],
    url='https://github.com/chewett/RaspberryPiVcgencmd',
    license='MIT',
    author='Christopher Hewett',
    author_email='chewett@hotmail.co.uk',
    description='Python binding for the Raspberry Pi Vcgencmd command line executable',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
