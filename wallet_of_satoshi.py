from decimal import Decimal
import json
import requests

MiliSatoshi = Decimal


class WalletOfSatoshi:
    def __init__(self, username: str):
        self.username = username

    def well_known(self) -> str:
        url = f"https://walletofsatoshi.com/.well-known/lnurlp/{self.username}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        raise Exception("Error: Failed to fetch LNURLP data from Wallet of Satoshi")

    def payment_request(
        self, amount: MiliSatoshi = MiliSatoshi(1000), memo: str = ""
    ) -> str:
        text = self.well_known()
        data = json.loads(text)
        url = data["callback"]

        response = requests.get(url, params={"amount": str(amount), "memo": memo})
        data = json.loads(response.text)
        pr = data["pr"]
        return pr
