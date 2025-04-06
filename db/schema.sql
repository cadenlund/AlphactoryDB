CREATE TABLE IF NOT EXISTS ohlcv_data (
    time         TIMESTAMPTZ NOT NULL,
    ticker       TEXT NOT NULL,
    open         DOUBLE PRECISION NOT NULL,
    close        DOUBLE PRECISION NOT NULL,
    high         DOUBLE PRECISION NOT NULL,
    low          DOUBLE PRECISION NOT NULL,
    volume       DOUBLE PRECISION NOT NULL,
    transactions BIGINT NOT NULL
);

