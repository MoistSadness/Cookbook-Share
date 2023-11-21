-- Creation of User table
CREATE TABLE IF NOT EXISTS Users (
    username    TEXT    NOT NULL,
    password    TEXT    NOT NULL,
    ssn         INT     NOT NULL
);

-- Use single quotes for string literals
INSERT INTO Users (username, password, ssn) VALUES
('Naruto', 'afdfadfa', 666),
('Sasuke', 'afdfadfa', 666),
('Sakura', 'afdfadfa', 666);