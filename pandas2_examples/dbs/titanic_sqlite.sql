-- Create the Titanic table
CREATE TABLE titanic (
    PassengerId INTEGER,
    Survived INTEGER,
    Pclass INTEGER,
    Name TEXT,
    Sex TEXT,
    Age REAL,
    SibSp INTEGER,
    Parch INTEGER,
    Ticket TEXT,
    Fare REAL,
    Cabin TEXT,
    Embarked TEXT
);

-- Import data from CSV file in the parent folder (update the path and file name if needed)
.mode csv
.import --skip 1 '../titanic.csv' titanic 
