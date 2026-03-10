CREATE TABLE IF NOT EXISTS contacts (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(20) NOT NULL CHECK (length(trim(first_name)) >= 2),
    last_name VARCHAR(20) NOT NULL CHECK (length(trim(last_name)) >= 2),
    phone VARCHAR(20) NOT NULL,
    note TEXT
);
