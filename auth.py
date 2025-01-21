import logging
import configs
import requests
import json

class AuthClient:
    def __init__(self):
        self.access_token = None
        self.id_token = None
        self.scope = None
        self.expires_in = None
        self.token_type = None
        self.authenticate()

    def authenticate(self):
        url = configs.AUTH_URL

        payload = json.dumps({
            "client_id": configs.CLIENT_ID,
            "client_secret": configs.CLIENT_SECRET,
            "grant_type": "password",
            "audience": configs.AUDIENCE,
            "username": configs.PATTODATEUSERNAME,
            "password": configs.PATTODATEPASSWORD,
            "scope": configs.SCOPE
        })
        headers = {
            'Content-Type': 'application/json'
        }

        logging.info(f"Authenticating with {url}")
        response = requests.post(url, headers=headers, data=payload)
        auth_response = response.json()
        self.access_token = auth_response.get("access_token")
        self.id_token = auth_response.get("id_token")
        self.scope = auth_response.get("scope")
        self.expires_in = auth_response.get("expires_in")
        self.token_type = auth_response.get("token_type")
