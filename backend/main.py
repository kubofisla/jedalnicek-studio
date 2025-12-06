import os
from flask import Flask, render_template
from database import db_util
from flask_cors import CORS

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    CORS(app)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db_util.init_app(app)

    import recipes
    app.register_blueprint(recipes.bp)

    import plan
    app.register_blueprint(plan.bp)

    import meals
    app.register_blueprint(meals.bp)

    import shoppingList
    app.register_blueprint(shoppingList.bp)

    import user_data
    app.register_blueprint(user_data.bp)

    import ingredients
    app.register_blueprint(ingredients.bp)

    return app