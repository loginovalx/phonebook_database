CREATE TABLE IF NOT EXISTS contacts (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(20) NOT NULL CHECK (length(trim(first_name)) <= 20),
    last_name VARCHAR(20) NOT NULL CHECK (length(trim(last_name)) <= 20),
    phone VARCHAR(20) NOT NULL,
    note TEXT
);
