-- script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server.
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = "california") ORDER BY id ASC;
