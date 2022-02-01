from setuptools import setup

setup(
    name="gym-mods",
    version="0.1.0",
    author="Filip Skubacz",
    author_email="filip.skubacz00@gmail.com",
    packages=["gym_mods"],
    license="LICENSE.md",
    description="Gym utilities and extensions",
    long_description=open("README.md").read(),
    install_requires=[
        "gym",
    ],
)
