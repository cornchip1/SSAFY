with tmp as (select 
  first_name,
  phone,
  country,
  case
    when length(phone) = 13 then substr(phone,5,4)
    when length(phone) = 12 then substr(phone,4,4)
  end as cq
from users)

select first_name, phone, country
from tmp
where cq like '51%' and country != '서울'