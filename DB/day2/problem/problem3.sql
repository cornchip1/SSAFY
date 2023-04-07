create table hotels (
  room_num text not null,
  check_in text not null,
  check_out text not null,
  grade text not null
  );


alter table hotels add column price INT not null default 0

insert into hotels 
values 
('B203','2021-12-31','2022-01-03','suite',900),
('1102','2022-01-04','2022-01-08','suite',850),
('303','2022-01-01','2022-01-03','deluxe',500),
('807','2021-01-04','2022-01-07','superior',300),
('B205','2022-01-04','2022-01-07','deluxe',550);

update hotels
set check_in = '2022-01-04'
where room_num = '807'

select *
from hotels
where room_num like 'B%' or grade = 'deluxe'