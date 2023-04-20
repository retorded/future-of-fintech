import os

from flask import Flask


# appfactory
def create_app(test_config=None):

    # create and configure the Flask instance
    app = Flask(__name__, instance_relative_config=True)

    # default config
    app.config.from_mapping(
        DATABASE=os.path.join(app.instance_path, 'empower.sqlite'),
    )

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'
    
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

    # registering db functions with the application
    from . import db
    db.init_app(app)

    # registering the blueprints
    from . import transformer, home
    app.register_blueprint(transformer.bp)
    app.register_blueprint(home.bp)
    app.add_url_rule('/', endpoint='index')

    return app
