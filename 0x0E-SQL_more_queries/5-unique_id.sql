-- Cretes a new table with a column having unique constraint
CREATE TABLE IF NOT EXISTS unique_id (
       id INT
       	  DEFAULT 1
       	  UNIQUE,
	name  VARCHAR(256)
);
