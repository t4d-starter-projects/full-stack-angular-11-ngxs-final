alter table employees
	add username varchar(255);

alter table employees
	add password varchar(255);

alter table categories alter column category_id type integer;
create sequence categories_category_id_seq owned by appdb.public.categories.category_id;
select setval('categories_category_id_seq', COALESCE((select MAX(category_id)+1 from categories), 1), false);
alter table categories alter column category_id SET default nextval('categories_category_id_seq');

alter table employees alter column employee_id type integer;
create sequence employees_employee_id_seq owned by appdb.public.employees.employee_id;
select setval('employees_employee_id_seq', COALESCE((select MAX(employee_id)+1 from employees), 1), false);
alter table employees alter column employee_id SET default nextval('employees_employee_id_seq');

alter table orders alter column order_id type integer;
create sequence orders_order_id_seq owned by appdb.public.orders.order_id;
select setval('orders_order_id_seq', COALESCE((select MAX(order_id)+1 from orders), 1), false);
alter table orders alter column order_id SET default nextval('orders_order_id_seq');

alter table products alter column product_id type integer;
create sequence products_product_id_seq owned by appdb.public.products.product_id;
select setval('products_product_id_seq', COALESCE((select MAX(product_id)+1 from products), 1), false);
alter table products alter column product_id SET default nextval('products_product_id_seq');

alter table region alter column region_id type integer;
create sequence region_region_id_seq owned by appdb.public.region.region_id;
select setval('region_region_id_seq', COALESCE((select MAX(region_id)+1 from region), 1), false);
alter table region alter column region_id SET default nextval('region_region_id_seq');

alter table shippers alter column shipper_id type integer;
create sequence shippers_shipper_id_seq owned by appdb.public.shippers.shipper_id;
select setval('shippers_shipper_id_seq', COALESCE((select MAX(shipper_id)+1 from shippers), 1), false);
alter table shippers alter column shipper_id SET default nextval('shippers_shipper_id_seq');

alter table suppliers alter column supplier_id type integer;
create sequence suppliers_supplier_id_seq owned by appdb.public.suppliers.supplier_id;
select setval('suppliers_supplier_id_seq', COALESCE((select MAX(supplier_id)+1 from suppliers), 1), false);
alter table suppliers alter column supplier_id SET default nextval('suppliers_supplier_id_seq');

alter table us_states alter column state_id type integer;
create sequence us_states_state_id_seq owned by appdb.public.us_states.state_id;
select setval('us_states_state_id_seq', COALESCE((select MAX(state_id)+1 from us_states), 1), false);
alter table us_states alter column state_id SET default nextval('us_states_state_id_seq');

alter table employee_territories alter column employee_id type integer;
alter table order_details alter column order_id type integer;
alter table order_details alter column product_id type integer;
alter table orders alter column employee_id type integer;
alter table products alter column supplier_id type integer;
alter table products alter column category_id type integer;
alter table territories alter column region_id type integer;

create table user_roles
(
	user_role_id serial not null,
	username varchar(255) not null,
	user_kind varchar(255) not null,
	role_id int not null
);

create unique index user_roles_user_role_id_uindex
	on user_roles (user_role_id);

alter table user_roles
	add constraint user_roles_pk
		primary key (user_role_id);

create table roles
(
	role_id serial not null,
	role_name varchar(255)
);

create unique index roles_role_id_uindex
	on roles (role_id);

alter table roles
	add constraint roles_pk
		primary key (role_id);

update employees set
  username = 'adodsworth',
  password = '$2b$12$chUG2YAgbEPNgpyK2DF3JOcnsPiFLkCRyfkNLP5Ue8SCzBe4TBGq6'
where
  employee_id = 9;

update employees set
  username = 'afuller',
  password = '$2b$12$chUG2YAgbEPNgpyK2DF3JOcnsPiFLkCRyfkNLP5Ue8SCzBe4TBGq6'
where
  employee_id = 2;

insert into roles (role_name) values('user');
insert into roles (role_name) values('admin');

insert into user_roles (username, user_kind, role_id) values ('adodsworth', 'employee', 1);
insert into user_roles (username, user_kind, role_id) values ('afuller', 'employee', 1);
insert into user_roles (username, user_kind, role_id) values ('afuller', 'employee', 2);