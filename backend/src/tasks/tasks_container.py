from dependency_injector import containers, providers

from .user.login_task import LoginTask
from .user.change_password_task import ChangePasswordTask
from .user.refresh_task import RefreshTask
from .user.has_one_or_more_roles_task import HasOneOrMoreRolesTask
from .crud.all_entities_task import AllEntitiesTask
from .crud.one_entity_by_id_task import OneEntityByIdTask
from .crud.append_entity_task import AppendEntityTask
from .crud.replace_entity_task import ReplaceEntityTask
from .crud.remove_entity_task import RemoveEntityTask


class Tasks(containers.DeclarativeContainer):
    adapters = providers.DependenciesContainer()

    login_user = providers.Factory(
        LoginTask,
        logging=adapters.logging,
        password_tools=adapters.password_tools,
        employees=adapters.employees
    )

    refresh_user = providers.Factory(
        RefreshTask,
        logging=adapters.logging,
        employees=adapters.employees
    )

    user_change_password = providers.Factory(
        ChangePasswordTask,
        logging=adapters.logging,
        password_tools=adapters.password_tools,
        employees=adapters.employees
    )

    user_has_one_or_more_roles = providers.Factory(
        HasOneOrMoreRolesTask,
        logging=adapters.logging,
        employees=adapters.employees
    )

    all_categories = providers.Factory(
        AllEntitiesTask,
        logging=adapters.logging,
        entities=adapters.categories
    )

    one_category_by_id = providers.Factory(
        OneEntityByIdTask,
        logging=adapters.logging,
        entities=adapters.categories
    )

    append_category = providers.Factory(
        AppendEntityTask,
        logging=adapters.logging,
        entities=adapters.categories
    )

    replace_category = providers.Factory(
        ReplaceEntityTask,
        logging=adapters.logging,
        entities=adapters.categories
    )

    remove_category = providers.Factory(
        RemoveEntityTask,
        logging=adapters.logging,
        entities=adapters.categories
    )

    all_suppliers = providers.Factory(
        AllEntitiesTask,
        logging=adapters.logging,
        entities=adapters.suppliers
    )

    one_supplier_by_id = providers.Factory(
        OneEntityByIdTask,
        logging=adapters.logging,
        entities=adapters.suppliers
    )

    append_supplier = providers.Factory(
        AppendEntityTask,
        logging=adapters.logging,
        entities=adapters.suppliers
    )

    replace_supplier = providers.Factory(
        ReplaceEntityTask,
        logging=adapters.logging,
        entities=adapters.suppliers
    )

    remove_supplier = providers.Factory(
        RemoveEntityTask,
        logging=adapters.logging,
        entities=adapters.suppliers
    )

    all_products = providers.Factory(
        AllEntitiesTask,
        logging=adapters.logging,
        entities=adapters.products
    )

    one_product_by_id = providers.Factory(
        OneEntityByIdTask,
        logging=adapters.logging,
        entities=adapters.products
    )

    append_product = providers.Factory(
        AppendEntityTask,
        logging=adapters.logging,
        entities=adapters.products
    )

    replace_product = providers.Factory(
        ReplaceEntityTask,
        logging=adapters.logging,
        entities=adapters.products
    )

    remove_product = providers.Factory(
        RemoveEntityTask,
        logging=adapters.logging,
        entities=adapters.products
    )

    all_employees = providers.Factory(
        AllEntitiesTask,
        logging=adapters.logging,
        entities=adapters.employees
    )

    one_employee_by_id = providers.Factory(
        OneEntityByIdTask,
        logging=adapters.logging,
        entities=adapters.employees
    )

    append_employee = providers.Factory(
        AppendEntityTask,
        logging=adapters.logging,
        entities=adapters.employees
    )

    replace_employee = providers.Factory(
        ReplaceEntityTask,
        logging=adapters.logging,
        entities=adapters.employees
    )

    remove_employee = providers.Factory(
        RemoveEntityTask,
        logging=adapters.logging,
        entities=adapters.employees
    )

    all_cars = providers.Factory(
        AllEntitiesTask,
        logging=adapters.logging,
        entities=adapters.cars
    )

    one_car_by_id = providers.Factory(
        OneEntityByIdTask,
        logging=adapters.logging,
        entities=adapters.cars
    )

    append_car = providers.Factory(
        AppendEntityTask,
        logging=adapters.logging,
        entities=adapters.cars
    )

    replace_car = providers.Factory(
        ReplaceEntityTask,
        logging=adapters.logging,
        entities=adapters.cars
    )

    remove_car = providers.Factory(
        RemoveEntityTask,
        logging=adapters.logging,
        entities=adapters.cars
    )

    all_colors = providers.Factory(
        AllEntitiesTask,
        logging=adapters.logging,
        entities=adapters.colors
    )

    one_color_by_id = providers.Factory(
        OneEntityByIdTask,
        logging=adapters.logging,
        entities=adapters.colors
    )

    append_color = providers.Factory(
        AppendEntityTask,
        logging=adapters.logging,
        entities=adapters.colors
    )

    replace_color = providers.Factory(
        ReplaceEntityTask,
        logging=adapters.logging,
        entities=adapters.colors
    )

    remove_color = providers.Factory(
        RemoveEntityTask,
        logging=adapters.logging,
        entities=adapters.colors
    )
