SELECT 
    u.user_id,
    u.username,
    u.user_location,
    p.post_id
FROM users u
JOIN posts p ON u.user_id = p.user_id
WHERE u.user_location = "Durham, NC";