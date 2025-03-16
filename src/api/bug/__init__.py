from flask import Blueprint, request

bug_blueprint = Blueprint("bug", __name__)


@bug_blueprint.route("/print-parameter", methods=["GET"])
def print_parameter():
    print(f"args: {request.args}")
    return request.args
