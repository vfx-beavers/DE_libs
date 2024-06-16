DROP DATABASE IF EXISTS de;
CREATE DATABASE de;
CREATE SCHEMA IF NOT EXISTS "tag" AUTHORIZATION pguser;

-- Очистка таблиц
DROP TABLE IF EXISTS tag.stg_sales cascade;
DROP TABLE IF EXISTS tag.stg_item cascade;
DROP TABLE IF EXISTS tag.stg_service cascade;
DROP TABLE IF EXISTS tag.stg_salesman cascade;
DROP TABLE IF EXISTS tag.stg_department cascade;

-- Создание таблиц
CREATE table tag.stg_item (
    id varchar(5) NULL,
	"name" varchar(50) NULL,
	price int NULL,
	sdate date NULL,
	edate date NULL,
	is_actual smallint null
);

CREATE table tag.stg_service (
    id varchar(5) NULL,
	"name" varchar(50) NULL,
	price int NULL,
	sdate date NULL,
	edate date NULL,
	is_actual smallint NULL
);

CREATE table tag.stg_department (
    filial_id smallint NULL,
	department_id smallint NULL,
	dep_chif_id smallint NULL
);

CREATE table tag.stg_salesman (
    id smallint null PRIMARY KEY,
	fio varchar(50) NULL,
	department_id smallint null 
);

CREATE table tag.stg_sales (
    sale_date date NULL,
	salesman_id smallint NULL,
	item_id varchar(5) NULL,
	quantity smallint NULL,
	final_price int null 
);

-- Заливка экспортированных csv в базу
COPY tag.stg_item FROM '/home/item.csv' WITH DELIMITER ',' CSV HEADER;
COPY tag.stg_service FROM '/home/service.csv' WITH DELIMITER ',' CSV HEADER;
COPY tag.stg_department FROM '/home/department.csv' WITH DELIMITER ',' CSV HEADER;
COPY tag.stg_salesman FROM '/home/salesman.csv' WITH DELIMITER ',' CSV HEADER;
COPY tag.stg_sales FROM '/home/sales.csv' WITH DELIMITER ',' CSV HEADER;