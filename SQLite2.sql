-- SQLite
SELECT id, guid, sent_at, sender_id, subject_id, SUBSTR(headers,1,10), SUBSTR(body,1,10)
FROM `Messages`;