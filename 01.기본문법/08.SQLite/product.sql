-- SQLite
CREATE TABLE product(
    code integer PRIMARY KEY AUTOINCREMENT,
    name char(100),
    price integer DEFAULT 0
);


SELECT * from product

INSERT INTO product(name,price)
VALUES('LG 세탁기',250000);
INSERT INTO product(name,price)
VALUES('LG 냉장고',350000);

