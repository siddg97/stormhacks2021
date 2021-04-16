from app.factory import create_flask
from app.utils.constants import USER_COOKIE_KEY

from tests.utils.test_factory import new_id


def get_test_app():
    """
    Retrieves an instance of the test client
    """
    app = create_flask(True)
    client = app.test_client()
    return client


def set_test_cookie(app, uid=None):
    """
    Sets a test cookie in the client based on a particular user id

    @param: app - instance of the test client
    @param: uid - user ID to generate a cookie against, one is generated if nothing is passed
    """
    if not uid:
        gen_uid = new_id()
        app.set_cookie("/", USER_COOKIE_KEY, gen_uid)
        return gen_uid

    app.set_cookie("/", USER_COOKIE_KEY, uid)
    return uid