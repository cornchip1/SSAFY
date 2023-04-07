-- drop table zoo;

CREATE TABLE zoo (
  name TEXT NOT NULL,
  eat TEXT NOT NULL,
  weight INT NOT NULL,
  height INT,
  age INT
);

INSERT INTO zoo VALUES 
('gorilla', 'omnivore', 215, 180, 5),
('tiger', 'carnivore', 220, 115, 3),
('elephant', 'herbivore', 3800, 280, 10),
('dog', 'omnivore', 8, 20, 1),
('panda', 'herbivore', 80, 90, 2),
('pig', 'omnivore', 70, 45, 5);

-- 1) 아무런 변화 없음
BEGIN;
  DELETE FROM zoo
  WHERE weight < 100;
ROLLBACK;

-- 2) eat = 'omnivore' 인 데이터 모두 삭제
BEGIN;
  DELETE FROM zoo
  WHERE eat = 'omnivore';
COMMIT;


-- 3) Result : 3
SELECT COUNT(*)
FROM zoo;

/*
query statement 를 실행하면 즉시 반영되는 특성이 있다. 
그러나 잘못된 조건을 설정했거나 쿼리문에 오류가 있음을 미처 인지하지 못한 채로 실행하게 된다면 database를 이전 상태로 되돌리기가 어렵다. 
이를 방지하기 위해 table을 수정하기 전 검증을 거치고, 검증 결과가 정상이라면 반영한다.
이 때 사용하는 명령어가 BEGIN ~ COMMIT/ROLLBACK 이다.

만약 BEGIN 문 이후의 쿼리를 검증했을 때 결과가 정상이라면 COMMIT 하여 서버에 반영하면 되고, 아니라면 ROLLBACK을 통해 이전 상태로 되돌린다.
따라서 1)의 쿼리문을 실행한다면 DB에는 아무런 변화가 없을 것이고, 2)의 쿼리문을 실행하면 eat = 'omnivore' 값을 가진 데이터는 모두 삭제될 것이다.

즉, 3번 쿼리의 결과값은 3이 된다.
*/