CREATE TABLE IF NOT EXISTS checks (
    id SERIAL PRIMARY KEY,
    url VARCHAR(1000) NOT NULL,
    response_time INTEGER NOT NULL,
    status_code INTEGER NOT NULL
);

CREATE INDEX ix_checks_url ON checks (url);
CREATE INDEX ix_checks_status_code ON checks (status_code);
