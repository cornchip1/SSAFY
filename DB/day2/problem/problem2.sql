create table zoo (
  name text not NULL,
  eat text not NULL,
  weight integer not NULL,
  height integer,
  age integer
);

insert into zoo
values
  ('gorilla','omnivore',215,180,5),
  ('rabbit','herbivore',3,150,''),
  ('tiger','carnivore',220,115,3),
  ('elephant','herbivore',3800,280,10),
  ('dog','omnivore',8,20,1),
  ('eagle','carnivore',8,75,''),
  ('dolphin','carnivore',210,'',3),
  ('alligator','carnivore',250,50,''),
  ('panda','herbivore',80,90,2),
  ('pig','omnivore',70,45,5);


select * from zoo

update zoo 
set height = 15
where name = 'rabbit'

delete from zoo where eat = 'omnivore'
select * from zoo