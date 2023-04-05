-- problem1
create table users_hw (
  name text not null,
  phoneNumber text not null,
  balance text not null,
  age integer,
  gender text
  );

-- problem2 (in terminal)
-- sqlite3
-- .mode csv
-- .import users.csv users_hw

-- problem3
select name, age, balance
from users_hw
order by age, balance desc