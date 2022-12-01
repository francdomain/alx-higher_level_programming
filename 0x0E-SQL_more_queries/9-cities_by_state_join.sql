-- lists all cities contained in the database hbtn_0d_usa.
-- states is the matching table, we collect all cities from cities table
SELECT cities.id, cities.name, states.name FROM cities LEFT JOIN states ON states.id = cities.state_id ORDER BY cities.id;
