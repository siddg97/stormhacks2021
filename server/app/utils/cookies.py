from flask import request, Response

from app.utils.constants import USER_COOKIE_KEY


def get_user_cookie():
    """
    Parses user id cookie for a request

    @returns: user id for mongo doc if found else None
    """
    user_id = request.cookies.get(USER_COOKIE_KEY)
    return user_id


def set_user_cookie(user_id):
    """
    Define callback to set the cookie headers for the response
    """

    def set_user_id(response):
        response.set_cookie(USER_COOKIE_KEY, user_id, httponly=True)
        return response

    return set_user_id