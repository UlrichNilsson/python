-- SQLite
SELECT id, email, sent_at, subject, SUBSTR(headers,1,10), SUBSTR(body,1,10)
FROM `Messages`;