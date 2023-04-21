DROP TABLE IF EXISTS plans;
DROP TABLE IF EXISTS consumption;
DROP TABLE IF EXISTS consumers;

CREATE TABLE plans (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  provider TEXT NOT NULL,
  pricingModel TEXT NOT NULL,
  monthlyFee REAL,
  price REAL NOT NULL,
  period INT,
  UNIQUE(provider, pricingModel)
);

CREATE TABLE consumption (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    consumer_id INTEGER NOT NULL,
    from_dt TIMESTAMP,
    to_dt TIMESTAMP,
    consumption REAL,
    unit TEXT,
    FOREIGN KEY (consumer_id) REFERENCES consumer (id)
);

CREATE TABLE consumers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    address TEXT
);






