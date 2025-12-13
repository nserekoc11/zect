class DerivError(Exception):
    """Base exception for pyderiv."""
    pass


class AuthorizationError(DerivError):
    pass


class DerivConnectionError(DerivError):
    pass

# Backwards compatible alias, avoid shadowing builtin ConnectionError
ConnectionError = DerivConnectionError
