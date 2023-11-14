import argparse

from .base_config import PartialConfig


class CliConnector:
    @staticmethod
    def build_config():
        parser = argparse.ArgumentParser(description="Keycraft CLI arguments.")
        parser.add_argument("--keycloak-url", help="URL of the Keycloak server")
        parser.add_argument("--admin-user", help="Keycloak admin username")
        parser.add_argument("--admin-password", help="Keycloak admin password")
        parser.add_argument("--realm-name", help="Name of the realm", default="MyRealm")
        parser.add_argument("--client-id", help="Client ID", default="my-client")
        args = parser.parse_args()

        return PartialConfig(
            keycloak_url=args.keycloak_url,
            admin_user=args.admin_user,
            admin_password=args.admin_password,
            realm_name=args.realm_name,
            client_id=args.client_id,
        )
