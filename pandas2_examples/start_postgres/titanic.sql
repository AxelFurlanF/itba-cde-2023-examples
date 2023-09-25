-- Titanic.sql
CREATE TABLE titanic(
    PassengerId INT,
    Survived INT,
    Pclass INT,
    Name TEXT,
    Sex TEXT,
    Age REAL,
    SibSp INT,
    Parch INT,
    Ticket TEXT,
    Fare REAL,
    Cabin TEXT,
    Embarked CHAR(1)
);

\copy titanic FROM '../titanic.csv' DELIMITER ',' CSV HEADER;
