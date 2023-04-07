create table animals (
  animal_name text not null,
  height integer not null,
  weight integer not null,
  age integer
);

alter table animals add column meal text null 

alter table animals rename column animal_name to name

alter table animals rename to zoo 

drop table zoo