
-- CREATE TABLE person(
--  	id BIGSERIAL NOT NULL PRIMARY KEY,
--   	first_name VARCHAR(50) NOT NULL,
--   	last_name VARCHAR(50) NOT NULL,
--   	gender VARCHAR(7) NOT NULL,
--   	email VARCHAR(100) NOT NULL UNIQUE,
--   	phone_number BIGINT NOT NULL UNIQUE,
-- 	date_of_birht TIMESTAMP DEFAULT NOW()
-- );


-- INSERT INTO person(first_name, last_name, gender, email, phone_number)
--  			VALUES('goutham', 'boine', 'male', 'goutham@gmail.com', 98765433);

SELECT * FROM PERSON;

-- ALTER TABLE PERSON RENAME COLUMN date_of_birht TO user_created;

