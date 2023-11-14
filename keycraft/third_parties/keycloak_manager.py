import logging

import requests

from keycraft.config.base_config import Config
from keycraft.exceptions import (AuthenticationError, ClientCreationError,
                                 RealmCreationError)


class KeycloakManager:
    def __init__(self, config: Config):
        self.config = config
        logging.info("KeycloakManager initialized with provided configuration.")

    def get_token(self):
        url = f"{self.config.keycloak_url}/realms/master/protocol/openid-connect/token"
        data = {
            "username": self.config.admin_user,
            "password": self.config.admin_password,
            "grant_type": "password",
            "client_id": "admin-cli",
        }
        try:
            response = requests.post(url, data=data)
            response.raise_for_status()
            logging.info("Successfully authenticated with Keycloak.")
        except requests.HTTPError as http_err:
            raise AuthenticationError(f"HTTP error during authentication: {http_err}")
        except Exception as e:
            raise AuthenticationError(f"Error during authentication: {e}")

        return response.json()["access_token"]

    def create_realm(self, token):
        url = f"{self.config.keycloak_url}/admin/realms"
        headers = {"Authorization": f"Bearer {token}"}
        data = {"realm": self.config.realm_name, "enabled": True}
        try:
            response = requests.post(url, headers=headers, json=data)
            response.raise_for_status()
            logging.info("Realm created successfully.")
        except requests.HTTPError as http_err:
            raise RealmCreationError(f"HTTP error during realm creation: {http_err}")
        except Exception as e:
            raise RealmCreationError(f"Error during realm creation: {e}")

    def create_client(self, token):
        url = (
            f"{self.config.keycloak_url}/admin/realms/{self.config.realm_name}/clients"
        )
        headers = {"Authorization": f"Bearer {token}"}
        data = {
            "id": self.config.client_id,
        }
        try:
            response = requests.post(url, headers=headers, json=data)
            response.raise_for_status()
        except requests.HTTPError as http_err:
            raise ClientCreationError(f"HTTP error during client creation: {http_err}")
        except Exception as e:
            raise ClientCreationError(f"Error during client creation: {e}")
