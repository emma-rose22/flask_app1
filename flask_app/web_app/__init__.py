from flask import Flask

#moves route definitions to another location
from web_app.routes.home_routes import home_routes

#function returns an app
def create_app():
    app = Flask(__name__)
    #you may want to look into blueprint objects, which allow us to store
    #definitions of several routes
    #then we take those routes and register them to our app
    
    app.register_blueprint(home_routes)
    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)