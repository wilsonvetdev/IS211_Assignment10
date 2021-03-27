CREATE TABLE artists (
    id INTEGER PRIMARY KEY ASC,
    artist_name TEXT
);

CREATE TABLE albums (
    id INTEGER PRIMARY KEY ASC,
    album_name TEXT,
    artist_id INTEGER
);

CREATE TABLE songs (
    id INTEGER PRIMARY KEY ASC,
    album_id INTEGER,
    song_title TEXT,
    song_num INTEGER,
    song_length INTEGER
)