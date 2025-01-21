import logging
from auth import AuthClient
import requests
import configs

class RequestClient:
    def __init__(self):
        self.access_token = None
        self.auth_client = AuthClient()
        self.access_token = self.auth_client.access_token

    def send_request(self, path):
        if not self.access_token:
            raise ValueError("Access token is not available. Please authenticate first.")

        headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json'
        }
        logging.info(f"Sending request to {configs.BE_ENDPOINT}/{path}")
        response = requests.get(f'{configs.BE_ENDPOINT}/{path}', headers=headers)
        return response.json()