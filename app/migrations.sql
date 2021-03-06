
CREATE TABLE IF NOT EXISTS word(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    label VARCHAR(255) UNIQUE,
    weight DOUBLE PRECISION
);

CREATE TABLE IF NOT EXISTS document(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    link VARCHAR(255) UNIQUE
);

CREATE TABLE IF NOT EXISTS word_document_assotiation(
    document_id INTEGER NOT NULL,
    word_id INTEGER NOT NULL,
    coefficient DOUBLE PRECISION NOT NULL,
    FOREIGN KEY(document_id)
        REFERENCES document(id)
        ON DELETE CASCADE,
    FOREIGN KEY(word_id)
        REFERENCES word(id)
        ON DELETE CASCADE,
    PRIMARY KEY (word_id, document_id)
);