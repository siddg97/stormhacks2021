from app.errors import HttpError
import traceback


def register_error_handlers(app):
    @app.errorhandler(HttpError)
    def handle_not_found(err):
        response = {
            "description": err.description,
            "code": err.code,
        }
        return response, err.code

    @app.errorhandler(Exception)
    def something_went_wrong(err):
        app.logger.error(f"Unhandled Exception: {str(err)}")
        # app.logger.debug(
        #     "".join(
        #         traceback.format_exception(
        #             etype=type(err), value=err, tb=err.__traceback__
        #         )
        #     )
        # )
        response = {"error": "something went wrong", "code": 500}
        return response, 500

    return app