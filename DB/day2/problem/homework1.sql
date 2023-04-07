CREATE TABLE zoo (
  name TEXT NOT NULL,
  eat TEXT NOT NULL,
  weight INT NOT NULL,
  height INT,
  age INT
);

-- 1) table의 column 순서과 다르게 data를 insert 하고 있다. 
-- insert into {table name} 다음에 () 안에 입력 순서대로 column 명을 나열해주거나, 데이터 입력 순서를 바꿔야 한다

INSERT INTO zoo VALUES 
-- (5, 180, 210, 'gorilla', 'omnivore');
('gorilla','omnivore',210,180,5);

-- 2) table에는 rowid column 이 없다. rowid column 을 먼저 만들어줘야 한다

ALTER TABLE zoo ADD COLUMN rowid int PRIMARY KEY;

INSERT INTO zoo (rowid, name, eat, weight, age) VALUES
(10,'dolphin', 'carnivore', 210, 3),
(10, 'alligator', 'carnivore', 250, 50);

-- 3) weight column 은 비어있는 상태로 둘 수 없는데, 하기의 예시에서는 weight column 이 비어있다
-- weight column 값을 넣어주거나, column 의 default value 를 0 등 임의의 값으로 설정해주면 된다.

-- INSERT INTO zoo1 (name, eat, age) VALUES
-- ('dolphin', 'carnivore', 3);
INSERT INTO zoo (name, eat, age, weight) VALUES
('dolphin', 'carnivore', 3, 0);


-- drop table zoo1