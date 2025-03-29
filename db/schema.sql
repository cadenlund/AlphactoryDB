-- Create hypertable for OHLCV
CREATE TABLE ohlcv_data (
    time        TIMESTAMPTZ       NOT NULL,
    symbol      TEXT              NOT NULL,
    open        DOUBLE PRECISION  NOT NULL,
    high        DOUBLE PRECISION  NOT NULL,
    low         DOUBLE PRECISION  NOT NULL,
    close       DOUBLE PRECISION  NOT NULL,
    volume      DOUBLE PRECISION  NOT NULL,
    PRIMARY KEY (time, symbol)
);
SELECT create_hypertable('ohlcv_data', 'time');

-- Create standard table for stock metadata
CREATE TABLE stock_metadata (
    ticker TEXT PRIMARY KEY,
    name TEXT,
    market_cap BIGINT,
    primary_exchange TEXT,
    type TEXT,
    share_class_shares_outstanding BIGINT,
    weighted_shares_outstanding BIGINT,
    active BOOLEAN
);

