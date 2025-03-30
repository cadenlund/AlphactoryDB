CREATE TABLE stock_metadata (
    ticker TEXT PRIMARY KEY,
    active BOOLEAN,
    type TEXT,
    market_cap NUMERIC,
    primary_exchange TEXT,
    sic_description TEXT,
    list_date DATE,
    name TEXT,
    description TEXT,
    total_employees INTEGER,
    share_class_shares_outstanding BIGINT,
    weighted_shares_outstanding BIGINT
);

CREATE TABLE ohlcv_data (
    time TIMESTAMPTZ NOT NULL,
    ticker TEXT REFERENCES stock_metadata(ticker),
    open NUMERIC,
    high NUMERIC,
    low NUMERIC,
    close NUMERIC,
    volume BIGINT,
    PRIMARY KEY (time, ticker)
);
SELECT create_hypertable('ohlcv_data', 'time');

