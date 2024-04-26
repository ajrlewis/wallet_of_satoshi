# WalletOfSatoshi

![My Project Logo](images/logo.png)

A package to use with your Wallet of Satoshi application instance.

## Installation

Install via pip:

```bash
pip install git+https://github.com/ajrlewis/wallet_of_satoshi.git
```

## Usage

Create an instance of `WalletOfSatoshi` and pass the `username` of your Wallet of Satoshi's account to its constructor!

The instance will expose two methods that are linked to this account:

1. `wallet_of_satoshi.well_known`

The "well-known" lightning address method returns the required response to satisfy the lightning address protocol. Put another way, this method returns the lightning address response from the Wallet of Satoshi website linked to your username!

2. `wallet_of_satoshi.pay_request`

Somewhat hacky method that returns a lightning invoice for your Wallet of Satoshi account for a given amount only. This method exploits the callback attribute of a valid lightning address response returned in the above method in order to ask for a lightning invoice of a specified amount.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
