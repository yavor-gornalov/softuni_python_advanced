ALLOWED_DOMAINS = [".com", ".bg", ".org", ".net"]
MIN_USERNAME_LENGTH = 4


class NameTooShortError(Exception):
    default_message = "Name must be more than 4 characters"

    def __init__(self, message=None):
        if message is None:
            message = self.default_message
        super().__init__(message)


class MustContainAtSymbolError(Exception):
    default_message = "Email must contain @"

    def __init__(self, message=None):
        if message is None:
            message = self.default_message
        super().__init__(message)


class InvalidDomainError(Exception):
    default_message = f"Domain must be one of the following: {', '.join(ALLOWED_DOMAINS)}"

    def __init__(self, message=None):
        if message is None:
            message = self.default_message
        super().__init__(message)


email_address = input()
while email_address != "End":
    if "@" not in email_address:
        raise MustContainAtSymbolError

    username, domain = email_address.split("@")

    if len(username) <= MIN_USERNAME_LENGTH:
        raise NameTooShortError

    for d in ALLOWED_DOMAINS:
        if domain.endswith(d):
            break
    else:
        raise InvalidDomainError

    print("Email is valid")
    email_address = input()
