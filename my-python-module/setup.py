from setuptools import setup, find_packages

setup(
    name='my-python-module',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A module for user administration functionalities',
    packages=find_packages(),
    install_requires=[
        'psutil',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)