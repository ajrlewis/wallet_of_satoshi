# wallet_of_satoshi

![My Project Logo](images/logo.png)

A python package to connect to your Wallet of Satoshi application.

## Installation

Install via pip:

```bash
pip install git+https://github.com/ajrlewis/wallet_of_satoshi.git
```

## Usage

Create an instance of `WalletOfSatoshi` and pass the `username` of your Wallet of Satoshi's account to its constructor!

```python
from wallet_of_satoshi import WalletOfSatoshi
wos = WalletOfSatoshi(username="your-wallet-of-satoshi-username")
```

The instance will expose you to two methods that are linked to your account:

1. `wos.well_known`

The "well-known" lightning address method returns the required response to satisfy the lightning address protocol. Put another way, this method returns the lightning address response from the Wallet of Satoshi website linked to your username!

2. `wos.pay_request`

Somewhat hacky method that returns a lightning invoice for your Wallet of Satoshi account for a given amount only. This method exploits the callback attribute of a valid lightning address response returned in the above method in order to ask for a lightning invoice of a specified amount.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

Note that the usage of this code is still under the MIT license, but you must also comply with the license terms of "Wallet of Satoshi".
