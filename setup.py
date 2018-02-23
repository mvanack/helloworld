
from setuptools import setup, find_packages
setup(
    name="helloworld",
    version="0.1",
    packages=find_packages(),
    author="Meredith VanAcker",
    license="GPLv3",
    description="A package for prepping for a movie",
    entry_points={
        'console_scripts': ['helloworld = helloworld.__main__:main']
        }
)