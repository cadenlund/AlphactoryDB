-- Create table for storing candle data
CREATE TABLE IF NOT EXISTS candles (
    ticker TEXT NOT NULL,
    time TIMESTAMPTZ NOT NULL,
    open DOUBLE PRECISION,
    high DOUBLE PRECISION,
    low DOUBLE PRECISION,
    close DOUBLE PRECISION,
    volume BIGINT,
    PRIMARY KEY (ticker, time)
);

-- Make it a hypertable (important for TimescaleDB!)
SELECT create_hypertable('candles', 'time', if_not_exists => TRUE);

