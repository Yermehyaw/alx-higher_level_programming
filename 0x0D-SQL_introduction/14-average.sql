-- Computes the average of all score records in second_table
ALTER TABLE second_table
ADD COLUMN average FLOAT;

CREATE TABLE IF NOT EXISTS tmp_table AS
SELECT AVG(scores) AS average
FROM second_table;

-- Update second_table with the average values of scores gotten via tmp_table
UPDATE second_table
SET average = (
    SELECT average
    FROM tmp_table);

-- Dispay new column added
SELECT average
FROM second_table

-- Delete temporary table
DROP TEMPORARY TABLE tmp_table;
