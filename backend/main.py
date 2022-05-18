import os

from flask import Flask
from database import db
#PAGES imports
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

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

    db.init_app(app)

    import recipes
    app.register_blueprint(recipes.bp)

    @app.route("/hello")
    def helloWorld():
        return "<h1>HELLO WORLD</h1>"

    @app.route('/plan', methods=['GET', 'POST'])
    def plan():
        database = db.get_db()
        return render_template('plan.html')

    return app