from flask import Flask, jsonify

from src.core.core_container import Adapters
from src.tasks.tasks_container import Tasks
from src.endpoints.apis import category_api as category_api_module
from src.endpoints.apis import employee_api as employee_api_module
from src.endpoints.apis import product_api as product_api_module
from src.endpoints.apis import supplier_api as supplier_api_module
from src.endpoints.apis import user_api as user_api_module
from src.endpoints.apis import color_api as color_api_module
from src.endpoints.apis import car_api as car_api_module


def create_app() -> Flask:
    adapters = Adapters()
    adapters.config.from_ini('config.ini')

    tasks = Tasks(adapters=adapters)
    tasks.wire([
        category_api_module,
        employee_api_module,
        product_api_module,
        supplier_api_module,
        user_api_module,
        color_api_module,
        car_api_module,
    ])

    # creating the Flask application
    rest_app = Flask(__name__, static_folder=None)
    rest_app.config['SECRET_KEY'] = adapters.config()['jwt']['secret_key']
    rest_app.tasks = tasks

    adapters.bcrypt().init_app(rest_app)

    # register the REST API endpoints
    rest_app.register_blueprint(category_api_module.category_api)
    rest_app.register_blueprint(employee_api_module.employee_api)
    rest_app.register_blueprint(product_api_module.product_api)
    rest_app.register_blueprint(supplier_api_module.supplier_api)
    rest_app.register_blueprint(user_api_module.user_api)
    rest_app.register_blueprint(color_api_module.color_api)
    rest_app.register_blueprint(car_api_module.car_api)

    return rest_app


app = create_app()


@app.errorhandler
def handle_internal_server_error(e):
    app.logger.error(e)
    return jsonify(''), 500
