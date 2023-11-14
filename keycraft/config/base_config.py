from typing import Optional


class PartialConfig:
    __slots__ = (
        "keycloak_url",
        "admin_user",
        "admin_password",
        "realm_name",
        "client_id",
    )

    keycloak_url: Optional[str]
    admin_user: Optional[str]
    admin_password: Optional[str]
    realm_name: Optional[str]
    client_id: Optional[str]

    def __init__(
        self,
        keycloak_url: Optional[str] = None,
        admin_user: Optional[str] = None,
        admin_password: Optional[str] = None,
        realm_name: Optional[str] = None,
        client_id: Optional[str] = None,
    ):
        self.keycloak_url = keycloak_url
        self.admin_user = admin_user
        self.admin_password = admin_password
        self.realm_name = realm_name
        self.client_id = client_id


class Config:
    __slots__ = (
        "keycloak_url",
        "admin_user",
        "admin_password",
        "realm_name",
        "client_id",
    )

    keycloak_url: str
    admin_user: str
    admin_password: str
    realm_name: str
    client_id: str

    def __init__(
        self,
        keycloak_url: str,
        admin_user: str,
        admin_password: str,
        realm_name: str,
        client_id: str,
    ):
        self.keycloak_url = keycloak_url
        self.admin_user = admin_user
        self.admin_password = admin_password
        self.realm_name = realm_name
        self.client_id = client_id
