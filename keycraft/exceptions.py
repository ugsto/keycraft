class KeycloakError(Exception):
    """Base class for Keycloak exceptions"""

    pass


class AuthenticationError(KeycloakError):
    """Raised when authentication fails"""

    pass


class RealmCreationError(KeycloakError):
    """Raised when realm creation fails"""

    pass


class ClientCreationError(KeycloakError):
    """Raised when client creation fails"""

    pass


class ConfigurationError(KeycloakError):
    """Raised when configuration fails"""

    pass
