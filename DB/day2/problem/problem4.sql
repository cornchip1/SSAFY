create table users(
  id int PRIMARY KEY,
  first_name text,
  last_name text,
  age int not null DEFAULT 0,
  country text not null,
  phone text,
  balance int not null DEFAULT 0
);


insert into users
values
  (1,'미현','김',19,'경기도','011-211-8482',300),
  (2,null,'최',33,'제주특병자치도',null,300),
  (3,'미숙','이',21,'서울특별시','010-2122-4958',480),
  (4,'남석','박',18,'경기도','011-484-8667',260),
  (5,'철수','박',45,'경상남도','016-295-8989',500),
  (6,null,'박',45,'전라북도',null,320),
  (7,'민준','이',35,'전라남도','019-965-8833',350),
  (8,null,'남',24,'충청남도','010-5882-5969',210),
  (9,'신','유',29,'경상북도','010-4949-2848',290),
  (10,null,'김',18,'대전광역시',null,300);

select id, age, balance
from users
where age < 25
order by age desc, balance;

select first_name,balance
from users
where first_name is not null and balance > 400;


UPDATE users
set phone = '알 수 없음'
where phone is null;

select *
from users;