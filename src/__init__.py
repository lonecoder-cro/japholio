#!python3

try:
    from flask import Flask
    from .config import Config
except ImportError as e:
    raise Exception(str(e))


def create_app(config_class=Config):
    try:
        from .views import home_view
    except ImportError as e:
        raise Exception(str(e))

    app = Flask(__name__, template_folder=None, static_folder=None)
    app.config.from_object(config_class)

    # Registering routes
    _routes = [home_view]
    for routes in _routes:
        app.register_blueprint(routes)

    return app
