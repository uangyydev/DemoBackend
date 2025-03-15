from flask import Blueprint, request

# 创建一个蓝图实例
main_routes = Blueprint("main", __name__)


# 定义路由
@main_routes.route("/")
def home():
    return "Hello, World!"


@main_routes.route("/print-cookies")
def print_cookies():
    print(request.cookies)
    return request.cookies
