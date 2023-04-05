SELECT *
FROM users
WHERE 
  country not in ('경기도','강원도') 
  and age >= 20 and age <= 30
ORDER BY age asc