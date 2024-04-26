from decimal import Decimal
import json
import requests
from typing import Any

MiliSatoshi = Decimal


class WalletOfSatoshi:
    """
    Wrapper class for interacting with the Wallet of Satoshi website API.
    """

    def __init__(self, username: str):
        """
        Initializes the WalletOfSatoshi object.

        Args:
            username: Wallet of Satoshi app-generated username.
        """
        self.username = username

    @property
    def well_known_url(self):
        return f"https://walletofsatoshi.com/.well-known/lnurlp/{self.username}"

    def well_known(self) -> dict[str, Any]:
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
            if "callback" not in data.keys():
                pass
            else:
                return data
        raise Exception(f"Failed to fetch LNURLP data from {self.well_known_url}.")

    def pay_request(self, amount: MiliSatoshi = MiliSatoshi(1000)) -> str:
        """
        Indirectly generates a payment request exploiting the callback from the
        lightning address above,

        Args:
            amount: Amount in mSatoshis (optional, default is 1000).

        Returns:
            The payment request.

        Raises:
            Exception: If there is an error generating the payment request.
        """
        data = self.well_known()  # Get the lightning address response
        url = data[
            "callback"
        ]  # Extract the lightning service URL for creating a payment request
        response = requests.get(url, params={"amount": str(amount)})
        if response.status_code == 200:
            data = response.json()
            return data
        raise Exception("Error: Failed to fetch payment request")
