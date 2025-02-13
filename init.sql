CREATE TABLE IF NOT EXISTS users (
    id BIGSERIAL PRIMARY KEY,
    username VARCHAR(30),
    password VARCHAR(30)
);

CREATE TABLE IF NOT EXISTS telegram_relationships (
    id BIGINT UNIQUE,  -- Это поле должно быть уникальным и может быть внешним ключом
    telegram_id BIGINT UNIQUE,  -- Уникальный идентификатор Telegram
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    FOREIGN KEY (id) REFERENCES users(id)  -- Связь с таблицей users
);

CREATE TABLE IF NOT EXISTS telegram_profile (
    telegram_id BIGINT UNIQUE,  -- Уникальный идентификатор Telegram
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    FOREIGN KEY (telegram_id) REFERENCES telegram_relationships(telegram_id)  -- Связь с telegram_relationships
);
