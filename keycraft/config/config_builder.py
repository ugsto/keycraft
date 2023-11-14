from keycraft.config.base_config import Config, PartialConfig
from keycraft.exceptions import ConfigurationError


class ConfigBuilder:
    __slots__ = ("partial_config",)

    def __init__(self):
        self.partial_config = PartialConfig()

    def merge(self, partial_config: PartialConfig):
        self.partial_config = PartialConfig(
            keycloak_url=self.partial_config.keycloak_url
            or partial_config.keycloak_url,
            admin_user=self.partial_config.admin_user or partial_config.admin_user,
            admin_password=self.partial_config.admin_password
            or partial_config.admin_password,
            realm_name=self.partial_config.realm_name or partial_config.realm_name,
            client_id=self.partial_config.client_id or partial_config.client_id,
        )

        return self

    def build(self) -> Config:
        if self.partial_config.keycloak_url is None:
            raise ConfigurationError("keycloak_url is required")
        if self.partial_config.admin_user is None:
            raise ConfigurationError("admin_user is required")
        if self.partial_config.admin_password is None:
            raise ConfigurationError("admin_password is required")
        if self.partial_config.realm_name is None:
            raise ConfigurationError("realm_name is required")
        if self.partial_config.client_id is None:
            raise ConfigurationError("client_id is required")

        return Config(
            keycloak_url=self.partial_config.keycloak_url,
            admin_user=self.partial_config.admin_user,
            admin_password=self.partial_config.admin_password,
            realm_name=self.partial_config.realm_name,
            client_id=self.partial_config.client_id,
        )
