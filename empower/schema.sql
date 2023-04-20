DROP TABLE IF EXISTS plans;


CREATE TABLE plans (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  provider TEXT UNIQUE NOT NULL,
  pricingModel TEXT NOT NULL,
  monthlyFee REAL,
  price REAL NOT NULL,
  period INT

);





