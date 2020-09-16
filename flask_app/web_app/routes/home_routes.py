from flask import Blueprint

home_routes = Blueprint("home_routes", __name__)

#again defining (decorating) the routes
#but we are assigning it to the blueprint instead of to the app directly
@home_routes.route('/')
def index():
    x = 2 + 5
    return f"Hello World! {x}"

@home_routes.route('/about')
def about():
    return "About Me"