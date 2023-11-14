import logging

from keycraft.config.config_loader import ConfigLoader
from keycraft.exceptions import ConfigurationError, KeycloakError
from keycraft.third_parties.keycloak_manager import KeycloakManager


class CliClient:
    def __init__(self):
        try:
            self.config = ConfigLoader.load_config()
        except ConfigurationError as e:
            print(f"Configuration Error: {e}")
            exit(1)

        self.keycloak_manager = KeycloakManager(self.config)

    def run(self):
        try:
            token = self.keycloak_manager.get_token()
            self.keycloak_manager.create_realm(token)
            self.keycloak_manager.create_client(token)
        except KeycloakError as e:
            logging.error(e)
