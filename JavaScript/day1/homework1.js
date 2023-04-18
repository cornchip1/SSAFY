// 1번
const nums = [1,2,3,4,5,6,7,8]

console.log('1번 출력 결과')
for (let i = 0; i < nums.length; i++) {
  console.log('nums[' + i + ']: ' + nums[i])
}
console.log()
// for (const i = 0; i < nums.length; i++) {
//                                     ^

// TypeError: Assignment to constant variable.

/* 
const를 사용해서 변수를 선언하는 경우, 값을 재정의할 수 없기 때문에 에러가 발생한다.
let 을 사용해서 변수를 선언해서 i 값이 변화할 수 있도록 한다. 
*/

// 2번
console.log('2번 출력 결과')
for (num of nums) {
  console.log(num, typeof num)
  // 출력 결과
  // 0 string
  // 1 string
  // 2 string
  // 3 string
  // 4 string
  // 5 string
  // 6 string
  // 7 string
}

/*
for ~ in 의 경우 속성 이름을 통해 반복하기 때문에 string 으로 나타난다.
반면, for ~ of 의 경우 속성 값을 통해 반복하기 때문에 type 을 number 로 인식한다
*/