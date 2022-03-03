import logging
import secrets
import hmac
import hashlib
import base64
from keys import Keys
import requests


class PrivacyLeptHost:
    @staticmethod
    def notify():
        try:
            crc_token = secrets.token_urlsafe(32)
            nonce = secrets.token_urlsafe(32)
            message = f"crc_token={crc_token}&nonce={nonce}"
            key = Keys.SECRET.encode("utf-8")
            hmac_result = hmac.new(key, message.encode("utf-8"), hashlib.sha256)
            signature = f"sha256={base64.b64encode(hmac_result.digest()).decode()}"
            host_type = "DESKTOP"

            response = requests.get(
                Keys.PRIVACY_LEPT_API,
                params={"crc_token": crc_token, "nonce": nonce},
                headers={
                    "privacy-lept-host-type": host_type,
                    "privacy-lept-signature": signature,
                },
            )

            response.raise_for_status()
            logging.info("notified")
        except Exception as e:
            logging.error(e)
