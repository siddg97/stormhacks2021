from app.errors import NotFoundError
from app.utils.cookies import get_user_cookie
from tasks.process_audio import process_audio_stats


def task_routes(app):
    @app.route("/api/tasks/<task_id>/status", methods=["GET"])
    def get_task_status(task_id):
        get_user_cookie(True)

        task = process_audio_stats.AsyncResult(task_id)
        if not task:
            raise NotFoundError()

        response = {"state": task.state, "result": {}}

        if task.state == "PENDING":
            response["current"] = 0
            response["total"] = 100
            response["status"] = "pending"
        elif task.state != "FAILURE":
            response["current"] = task.info.get("current", 0)
            response["total"] = task.info.get("total", 100)
            response["status"] = task.info.get("status", "")

            if "result" in task.info:
                response["result"] = task.info["result"]
        else:
            response["current"] = 100
            response["total"] = 100
            response["status"] = str(task.info)

        return response, 200