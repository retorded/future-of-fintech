DROP TABLE IF EXISTS plans;

CREATE TABLE plans (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  provider TEXT NOT NULL,
  pricingModel TEXT NOT NULL,
  monthlyFee REAL,
  price REAL NOT NULL,
  period INT,
  UNIQUE(provider, pricingModel)
);





