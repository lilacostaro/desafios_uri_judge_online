"""
Created on Thu Jan  6 03:45:03 2022

@author: camila

No Rental

The video store company intends to do a promotion for customers who have not yet done any rental.

Your job is to deliver us the ID and the name of the customers who have not done any rental. Sort the output by ID.
"""

select 
	customers.id,
	customers.name
from customers
left join locations ON customers.id = locations.id_customers
where locations.locations_date is null
order by customers.id;

--- In case you wanna try in your own database

--- URI Online Judge SQL
--- Copyright URI Online Judge
--- www.urionlinejudge.com.br
--- Problem 2616

CREATE TABLE customers (
  id numeric PRIMARY KEY,
  name varchar(50),
  street varchar(50),
  city varchar(50)
);


CREATE TABLE locations (
  id numeric PRIMARY KEY,
  locations_date date,
  id_customers numeric REFERENCES customers (id)
);

INSERT INTO customers (id, name, street, city)
VALUES
  (1,	'Giovanna Goncalves Oliveira',	'Rua Mato Grosso',	'Canoas'),
  (2,	'Kauã Azevedo Ribeiro',	'Travessa Ibiá',	'Uberlândia'),
  (3,	'Rebeca Barbosa Santos',	'Rua Observatório Meteorológico',	'Salvador'),
  (4,	'Sarah Carvalho Correia',	'Rua Antônio Carlos da Silva',	'Apucarana'),
  (5,	'João Almeida Lima',	'Rua Rio Taiuva',	'Ponta Grossa'),
  (6,	'Diogo Melo Dias',	'Rua Duzentos e Cinqüenta',	'Várzea Grande');
  

INSERT INTO locations (id , locations_date, id_customers)
VALUES
  (1,	'09/10/2016',	3),
  (2,	'02/09/2016',	1),
  (3,	'02/08/2016',	4),
  (4,	'02/09/2015',	2),
  (5,	'02/03/2016',	6),
  (6,	'04/04/2016',	4);
  

  /*  Execute this query to drop the tables */
  -- DROP TABLE locations, customers; --