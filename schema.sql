CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(100),
    email VARCHAR(120),
    password VARCHAR(255)
);

CREATE TABLE tasks (
    id SERIAL PRIMARY KEY,
    title VARCHAR(200),
    description TEXT,
    priority VARCHAR(50),
    status VARCHAR(50),
    created_date TIMESTAMP,
    user_id INTEGER REFERENCES users(id)
);
