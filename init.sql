CREATE table users (
id integer UNIQUE PRIMARY KEY NOT NULL,
username varchar(20) not null,
password varchar(2048) not null,
created_at timestamp default CURRENT_TIMESTAMP,
admin bool default 0
);

CREATE TABLE files (
id TEXT UNIQUE PRIMARY KEY NOT NULL,
user_id INTEGER,
file_name TEXT,
data BLOB,
created_at timestamp default CURRENT_TIMESTAMP,
FOREIGN KEY(user_id) REFERENCES users(id)
);