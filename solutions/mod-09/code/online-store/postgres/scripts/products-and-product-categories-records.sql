-- load data into the product tables

-- insert three product categories
INSERT INTO labsch.products_productcategory (prod_cat_name, prod_cat_code)
    VALUES ('Television', 'TV');
INSERT INTO labsch.products_productcategory (prod_cat_name, prod_cat_code)
    VALUES ('Monitor', 'MO');
INSERT INTO labsch.products_productcategory (prod_cat_name, prod_cat_code)
    VALUES ('Display', 'DI');

-- insert seven products
INSERT INTO labsch.products_product (prod_name, prod_status, prod_price, prod_count, prod_cat_id_id)
    VALUES ('LG 55-inch 4K Ultra HD Smart TV', 1, 456.00, 34, 1);
INSERT INTO labsch.products_product (prod_name, prod_status, prod_price, prod_count, prod_cat_id_id)
    VALUES ('Samsung 65-inch 4K Ultra HD Smart TV', 0, 340.56, 12, 1);
INSERT INTO labsch.products_product (prod_name, prod_status, prod_price, prod_count, prod_cat_id_id)
    VALUES ('Sony 75-inch 4K Ultra HD Smart TV', 1, 890.45, 5, 1);
INSERT INTO labsch.products_product (prod_name, prod_status, prod_price, prod_count, prod_cat_id_id)
    VALUES ('TCL 50-inch 4K Ultra HD Smart TV', 1, 340.40, 2, 1);
INSERT INTO labsch.products_product (prod_name, prod_status, prod_price, prod_count, prod_cat_id_id)
    VALUES ('Vizio 60-inch 4K Ultra HD Smart TV', 0, 500.30, 3, 1);
INSERT INTO labsch.products_product (prod_name, prod_status, prod_price, prod_count, prod_cat_id_id)
    VALUES ('MSI Optix 27-inch Full HD Gaming Monitor', 1, 123.40, 3, 2);
INSERT INTO labsch.products_product (prod_name, prod_status, prod_price, prod_count, prod_cat_id_id)
    VALUES ('ASUS 24-inch Full HD Monitor', 1, 67.45, 6, 2);
INSERT INTO labsch.products_product (prod_name, prod_status, prod_price, prod_count, prod_cat_id_id)
    VALUES ('Dell 27-inch Full HD Monitor', 0, 87.34, 9, 2);
INSERT INTO labsch.products_product (prod_name, prod_status, prod_price, prod_count, prod_cat_id_id)
    VALUES ('HP 22-inch Full HD Monitor', 1, 56.78, 2, 2);
INSERT INTO labsch.products_product (prod_name, prod_status, prod_price, prod_count, prod_cat_id_id)
    VALUES ('Samsung 32-inch Full HD Monitor', 0, 78.90, 3, 2);
INSERT INTO labsch.products_product (prod_name, prod_status, prod_price, prod_count, prod_cat_id_id)
    VALUES ('LG 24-inch Full HD Monitor', 1, 45.67, 2, 2);
INSERT INTO labsch.products_product (prod_name, prod_status, prod_price, prod_count, prod_cat_id_id)
    VALUES ('Dell 24-inch Full HD Monitor', 0, 67.89, 3, 2);
INSERT INTO labsch.products_product (prod_name, prod_status, prod_price, prod_count, prod_cat_id_id)
    VALUES ('Samsung 24-inch Full HD Monitor', 1, 45.67, 2, 2);
INSERT INTO labsch.products_product (prod_name, prod_status, prod_price, prod_count, prod_cat_id_id)
    VALUES ('LG 14-inch Full HD Monitor', 0, 67.89, 3, 2);
INSERT INTO labsch.products_product (prod_name, prod_status, prod_price, prod_count, prod_cat_id_id)
    VALUES ('Nummax LED Mini Poster', 1, 340.40, 2, 3);
INSERT INTO labsch.products_product (prod_name, prod_status, prod_price, prod_count, prod_cat_id_id)
    VALUES ('Barco JAO18 - MKII', 0, 500.30, 3, 3);

INSERT INTO labsch.products_product (prod_name, prod_status, prod_price, prod_count, prod_cat_id_id)
    VALUES ('Samsung 12-inch Poster', 1, 78.90, 3, 3);
INSERT INTO labsch.products_product (prod_name, prod_status, prod_price, prod_count, prod_cat_id_id)
    VALUES ('LG 27-inch FHD Display', 0, 45.67, 2, 3);
INSERT INTO labsch.products_product (prod_name, prod_status, prod_price, prod_count, prod_cat_id_id)
    VALUES ('Dell 24-inch Vertical Poster', 1, 67.89, 3, 3);
INSERT INTO labsch.products_product (prod_name, prod_status, prod_price, prod_count, prod_cat_id_id)
    VALUES ('Samsung 24-inch FHD Display', 0, 45.67, 2, 3);
INSERT INTO labsch.products_product (prod_name, prod_status, prod_price, prod_count, prod_cat_id_id)
    VALUES ('LG 24-inch Horizontal Poster', 1, 67.89, 3, 3);

COMMIT;
