import os

from .base_config import PartialConfig


class EnvConnector:
    @staticmethod
    def build_config():
        return PartialConfig(
            keycloak_url=os.environ.get("KEYCLOAK_URL"),
            admin_user=os.environ.get("KEYCLOAK_ADMIN_USER"),
            admin_password=os.environ.get("KEYCLOAK_ADMIN_PASSWORD"),
            realm_name=os.environ.get("KEYCLOAK_REALM_NAME", "MyRealm"),
            client_id=os.environ.get("KEYCLOAK_CLIENT_ID", "my-client"),
        )
