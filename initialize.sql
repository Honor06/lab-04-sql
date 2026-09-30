DROP TABLE IF EXISTS posts;
DROP TABLE IF EXISTS users;
CREATE TABLE users (
    user_id INT PRIMARY KEY,
    username VARCHAR(50),
    user_location TEXT
);

CREATE TABLE posts (
    post_id INT PRIMARY KEY,
    user_id INT,
    post_time DATETIME,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

INSERT INTO users (user_id, username, user_location)
VALUES (1454, "Alice", "Durham, NC");
INSERT INTO posts (post_id, user_id, post_time) 
VALUES (123456, 1454, "2026-09-30 10:00:00");
INSERT INTO users (user_id, username, user_location)
VALUES (1455, "Bob", "Durham, NC");
INSERT INTO posts (post_id, user_id, post_time) 
VALUES (123457, 1455, "2026-09-30 10:01:00");
INSERT INTO users (user_id, username, user_location)
VALUES (1456, "Charlie", "Los Angeles, CA");
INSERT INTO posts (post_id, user_id, post_time) 
VALUES (123458, 1456, "2026-09-30 10:02:00");
INSERT INTO users (user_id, username, user_location)
VALUES (1457, "David", "Chicago, IL");
INSERT INTO posts (post_id, user_id, post_time)
VALUES (123459, 1457, "2026-09-30 10:03:00");
INSERT INTO users (user_id, username, user_location)
VALUES (1458, "Eve", "Seattle, WA");
INSERT INTO posts (post_id, user_id, post_time)
VALUES (123460, 1458, "2026-09-30 10:04:00");
INSERT INTO users (user_id, username, user_location)
VALUES (1459, "Frank", "Boston, MA");
INSERT INTO posts (post_id, user_id, post_time)
VALUES (123461, 1459, "2026-09-30 10:05:00");
INSERT INTO users (user_id, username, user_location)
VALUES (1460, "Savannah", "Miami, FL");
INSERT INTO posts (post_id, user_id, post_time)
VALUES (123462, 1460, "2026-09-30 10:06:00");
INSERT INTO users (user_id, username, user_location)
VALUES (1461, "Henry", "San Francisco, CA");
INSERT INTO posts (post_id, user_id, post_time)
VALUES (123463, 1461, "2026-09-30 10:07:00");
INSERT INTO users (user_id, username, user_location)
VALUES (1462, "IvyMay", "Austin, TX");
INSERT INTO posts (post_id, user_id, post_time)
VALUES (123464, 1462, "2026-09-30 10:08:00");
INSERT INTO users (user_id, username, user_location)
VALUES (1463, "Jack", "Portland, OR");
INSERT INTO posts (post_id, user_id, post_time)
VALUES (123465, 1463, "2026-09-30 10:09:00");