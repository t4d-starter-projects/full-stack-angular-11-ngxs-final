from dependency_injector import containers, providers
from flask_bcrypt import Bcrypt

from .services.logging import Logging
from .services.pg_data_session import PgDataSession
from .services.password_tools import PasswordTools
from .services.entities import Entities
from .services.employees import Employees
from .entities.category import Category
from .entities.product import Product
from .entities.supplier import Supplier
from .entities.car import Car
from .entities.color import Color


class Adapters(containers.DeclarativeContainer):
    config = providers.Configuration()

    logging = providers.Factory(
        Logging,
    )

    bcrypt = providers.Factory(
        Bcrypt,
    )

    data_session = providers.Factory(
        PgDataSession,
        url=config.database.url,
        name=config.database.name,
        user=config.database.user,
        password=config.database.password
    )

    password_tools = providers.Factory(
        PasswordTools,
        bcrypt=bcrypt
    )

    categories = providers.Factory(
        Entities,
        logging=logging,
        data_session=data_session,
        model=Category,
        model_key_field='category_id'
    )

    employees = providers.Factory(
        Employees,
        logging=logging,
        data_session=data_session,
    )

    suppliers = providers.Factory(
        Entities,
        logging=logging,
        data_session=data_session,
        model=Supplier,
        model_key_field='supplier_id'
    )

    products = providers.Factory(
        Entities,
        logging=logging,
        data_session=data_session,
        model=Product,
        model_key_field='product_id'
    )

    cars = providers.Factory(
        Entities,
        logging=logging,
        data_session=data_session,
        model=Car,
        model_key_field='car_id'
    )

    colors = providers.Factory(
        Entities,
        logging=logging,
        data_session=data_session,
        model=Color,
        model_key_field='color_id'
    )
