-- script that inserts a new row in the table first_table (database hbtn_0c_0) in your MySQL server.
CREATE TABLE IF NOT EXISTS second_table like first_table;
ALTER TABLE IF EXISTS second_table ADD score INT;
INSERT INTO IF EXISTS second_table (`id`,`name`,`score`)
VALUES
(1, "John", 10),
(2, "Alex", 3),
(3, "Bob", 14),
(4, "George", 8);
