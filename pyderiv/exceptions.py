class DerivError(Exception):
    """Base exception for pyderiv."""
    pass


class AuthorizationError(DerivError):
    pass


class ConnectionError(DerivError):
    pass
