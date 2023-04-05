-- CREATE TABLE users (
--   first_name text not null,
--   last_name text not null,
--   age integer not null,
--   country text not NULL,
--   phone text not null,
--   balance integer not null
--   );

select 
  first_name,
  age,
  balance
from users
order by
  age asc,
  balance desc