DROP TABLE IF EXISTS matricula;

CREATE TABLE matricula (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    name TEXT NOT NULL,
    born TEXT NOT NULL,
    grad TEXT NOT NULL,
    sch TEXT,
    addr TEXT,
    city TEXT,
    uf TEXT,
    resp TEXT NOT NULL,
    email TEXT NOT NULL,
    tel TEXT NOT NULL,
    obs TEXT
);

DROP TABLE IF EXISTS login;

CREATE TABLE login (
    id TEXT PRIMARY KEY,
    pwd TEXT NOT NULL
);