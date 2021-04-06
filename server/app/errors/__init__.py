class HttpError(Exception):
    pass


class BadRequestError(HttpError):
    code = 400
    description = "bad request"


class NotFoundError(HttpError):
    code = 404
    description = "resource not found"


class ForbiddenError(HttpError):
    code = 401
    description = "fordidden, unauthorized"
