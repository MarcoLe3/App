CREATE TABLE IF NOT EXISTS events (
    id BIGSERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    genre TEXT NOT NULL,
    location TEXT NOT NULL,
    start_time TIMESTAMPTZ NOT NULL,
    end_time TIMESTAMPTZ,
    available_tickets INTEGER NOT NULL DEFAULT 0
)

CREATE TYPE ticket_status AS ENUM (
    'avaliable',
    'reserved',
    'sold'
)

CREATE TABLE IF NOT EXISTS tickets (
    id BIGSERIAL PRIMARY KEY,
    event_id BIGINT NOT NULL REFERENCES events(id),
    status ticket_status NOT NULL DEFAULT 'avaliable',
    user_id BIGINT REFERENCES user(id),
)

CREATE TABLE IF NOT EXISTS user (
    id BIGSERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
)

CREATE INDEX IF NOT EXISTS
ticket_event_id_index
    ON tickets(event_id)