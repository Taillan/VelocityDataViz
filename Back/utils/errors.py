# define Python user-defined exceptions
NOT_FOUND_USER = "User not found"
BAD_REQUEST_PASSWORD_MESSAGE = "Missing password field in JSON body"
WRONG_PASSWORD_MESSAGE = "Wrong password"
BAD_TOKEN_MESSAGE = "Error while parsing token, ensure it's in form : 'Bearer ...'"
WRONG_TOKEN_MESSAGE = "Wrong token, please reload it"
USER_CREATED_MESSAGE = "User successfully created"
INTERNAL_ERROR_MESSAGE = "Internal error : "
ALL_USER_DELETED_MESSAGE = "All users successfully deleted"
ALL_LIFT_DELETED_MESSAGE = "All lifts successfully deleted"

class Error(Exception):
    pass

class NotFound(Error):
    pass

class AlreadyExisting(Error):
    pass

class BadToken(Error):
    pass

class WrongToken(Error):
    pass

class BadParticipation(Error):
    pass