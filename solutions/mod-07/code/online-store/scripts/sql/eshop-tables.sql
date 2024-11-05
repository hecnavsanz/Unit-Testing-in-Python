-- eshop_db schema

-- DROP TABLE labsch.products_productcategory;

CREATE TABLE labsch.products_productcategory (
	prod_cat_id int4 GENERATED BY DEFAULT AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE) NOT NULL,
	prod_cat_name varchar(50) NOT NULL,
	prod_cat_code varchar(2) NOT NULL,
	CONSTRAINT products_productcategory_pkey PRIMARY KEY (prod_cat_id)
);

-- DROP TABLE labsch.products_product;

CREATE TABLE labsch.products_product (
	prod_id int4 GENERATED BY DEFAULT AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE) NOT NULL,
	prod_name varchar(100) NOT NULL,
	prod_status int4 NOT NULL,
	prod_price numeric(5, 2) NOT NULL,
	prod_count int4 NOT NULL,
	prod_cat_id_id int4 NOT NULL,
	CONSTRAINT products_product_pkey PRIMARY KEY (prod_id),
	CONSTRAINT products_product_prod_name_key UNIQUE (prod_name),
	CONSTRAINT products_product_prod_cat_id_id_e32aec79_fk_products_ FOREIGN KEY (prod_cat_id_id) REFERENCES labsch.products_productcategory(prod_cat_id) DEFERRABLE INITIALLY DEFERRED
);
CREATE INDEX products_product_prod_cat_id_id_e32aec79 ON labsch.products_product USING btree (prod_cat_id_id);
CREATE INDEX products_product_prod_name_b98793db_like ON labsch.products_product USING btree (prod_name varchar_pattern_ops);