from setuptools import find_packages, setup

setup(
    name='empower',
    version='1.0.0',
    author='tordn',
    url='https://github.com/retorded/',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)