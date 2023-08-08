from setuptools import setup, find_packages

setup(
    name="wallet_of_satoshi",
    version="0.1",
    packages=find_packages(),
    install_requires=["requests"],
    url="https://github.com/ajrlewis/wallet_of_satoshi",
    author="ajrlewis",
    author_email="hello@ajrlewis.com",
    description="Wallet of Satoshi API",
)
