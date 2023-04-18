DROP TABLE IF EXISTS providers;


CREATE TABLE providers (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  provider TEXT UNIQUE NOT NULL,
  pricingModel TEXT NOT NULL,
  variablePrice FLOAT NOT NULL,
  fixedPricePeriod INT NOT NULL
);



