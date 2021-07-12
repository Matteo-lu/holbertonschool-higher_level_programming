-- script that inserts a new row in the table first_table (database hbtn_0c_0) in your MySQL server.
CREATE TABLE IF NOT EXISTS second_table (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, name VARCHAR(20), score INT);
INSERT INTO first_table (`id`,`name`,`score`) VALUES (1, "John", 10);
INSERT INTO first_table (`id`,`name`,`score`) VALUES (2, "John", 3);
INSERT INTO first_table (`id`,`name`,`score`) VALUES (3, "John", 14);
INSERT INTO first_table (`id`,`name`,`score`) VALUES (4, "John", 8);
