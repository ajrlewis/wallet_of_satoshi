from decimal import Decimal
import json
import requests

MiliSatoshi = Decimal


class WalletOfSatoshi:
    """
    Wrapper class for interacting with Wallet of Satoshi API.
    """

    def __init__(self, username: str):
        """
        Initializes the WalletOfSatoshi object.

        Args:
            username: Wallet of Satoshi username.
        """
        self.username = username

    def well_known(self) -> str:
        """
        Fetches the LNURLP data from Wallet of Satoshi.

        Returns:
            The LNURLP data as a string.

        Raises:
            Exception: If there is an error fetching the LNURLP data.
        """
        url = f"https://walletofsatoshi.com/.well-known/lnurlp/{self.username}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        raise Exception("Error: Failed to fetch LNURLP data from Wallet of Satoshi")

    def payment_request(self, amount: MiliSatoshi = MiliSatoshi(1000)) -> str:
        """
        Generates a payment request.

        Args:
            amount: Amount in mSatoshis (optional, default is 1000).

        Returns:
            The payment request.

        Raises:
            Exception: If there is an error generating the payment request.
        """
        text = self.well_known()
        data = json.loads(text)
        url = data["callback"]
        response = requests.get(url, params={"amount": str(amount)})
        data = json.loads(response.text)
        pr = data["pr"]
        return pr
