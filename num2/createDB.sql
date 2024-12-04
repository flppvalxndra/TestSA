 /*
В системе хранится информация о заказах: кто является покупателем, что было куплено, 
время и его статус. Заказы проходят через определенную статусную модель: 
Новый (new) -> Согласование (coordination) -> Выполнено (done) или Отклонено (declined).

Также хранится информация о продуктах: название, описание, прейскурантная цена и категория товара. 
О клиенте фиксируются: название компании, контактные данные и ИНН. 
Также хранятся данные о менеджерах по продажам: ФИО, адрес электронной почты, телефон, должность и дата приема на работу.
*/

CREATE TABLE customers
( 
	cus_id	 integer PRIMARY KEY,
	name	 varchar(255),
	mail	 varchar(255),	 
	tin	     varchar(255),
	address	 varchar(255)
)

 CREATE TABLE orders
( 
	ord_id	    integer PRIMARY KEY,
	cus_id	    integer,
	status	    varchar(255),
	emp_id	    integer,	 
	ordered_at	datetime
)

CREATE TABLE employees
( 
	emp_id       integer PRIMARY KEY,
	full_name	 varchar(255),
	phone		 varchar(255),
	email		 varchar(255),
	hired_at	 datetime,
	position	 varchar(255)
)

CREATE TABLE order_items
( 
	ord_id	    integer,
	item_id	    integer,
	quantity	integer,
	product_id	integer,
	CONSTRAINT c1 PRIMARY KEY  CLUSTERED (ord_id ASC,item_id ASC),
)

CREATE TABLE products
( 
	prod_id	    integer PRIMARY KEY,
	name        varchar(255),
	description varchar(255),
	cat_id integer,
	price float
)

CREATE TABLE categories
( 
	cat_id integer PRIMARY KEY,
	name        varchar(255)
)

ALTER TABLE [orders]  ADD CONSTRAINT [fk1] FOREIGN KEY ([emp_id]) REFERENCES [employees]([emp_id]);
ALTER TABLE [orders]  ADD CONSTRAINT [fk0] FOREIGN KEY ([cus_id]) REFERENCES [customers]([cus_id]);
ALTER TABLE [order_items]  ADD CONSTRAINT [fk2] FOREIGN KEY ([ord_id]) REFERENCES [orders]([ord_id]);
ALTER TABLE [order_items] ADD CONSTRAINT [fk3] FOREIGN KEY ([product_id]) REFERENCES [products]([prod_id]);
ALTER TABLE [products] ADD CONSTRAINT [fk4] FOREIGN KEY ([cat_id]) REFERENCES [categories]([cat_id]);
