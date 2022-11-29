-- lists the number of records with the same score in the table second_table of the database hbtn_0c_0 in your MySQL server
SELECT COUNT(*) AS `number` WHERE score NOT DISTINCT ORDER BY `number` DESC;
