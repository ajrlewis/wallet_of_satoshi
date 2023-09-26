from decimal import Decimal
import json
import requests

MiliSatoshi = Decimal


class WalletOfSatoshi:
    """
    Wrapper class for interacting with the Wallet of Satoshi API.
    """

    def __init__(self, username: str):
        """
        Initializes the WalletOfSatoshi object.

        Args:
            username: Wallet of Satoshi username.
        """
        self.username = username
        self.well_known_url = (
            f"https://walletofsatoshi.com/.well-known/lnurlp/{self.username}"
        )

    def well_known(self) -> str:
        """
        Fetches the LNURLP data from the .well-known endpoint.

        Returns:
            The LNURLP data as a string.

        Raises:
            Exception: If there is an error fetching the LNURLP data.
        """
        response = requests.get(self.well_known_url)
        if response.status_code == 200:
            data = response.json()
            return data
        raise Exception("Error: Failed to fetch LNURLP data.")

    def pay_request(self, amount: MiliSatoshi = MiliSatoshi(1000)) -> str:
        """
        Generates a payment request.

        Args:
            amount: Amount in mSatoshis (optional, default is 1000).

        Returns:
            The payment request.

        Raises:
            Exception: If there is an error generating the payment request.
        """
        data = self.well_known()
        url = data["callback"]  # URL from LN SERVICE to accept pay request
        response = requests.get(url, params={"amount": str(amount)})
        if response.status_code == 200:
            data = response.json()
            return data
        raise Exception("Error: Failed to fetch payment request")
