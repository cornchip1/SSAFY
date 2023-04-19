/*
// 매개변수보다 인자의 개수가 적을 경우 (매개변수와 인자의 불일치 허용)
const threeArgs = function(arg1, arg2, arg3){
  return [arg1,arg2,arg3]
}

console.log(threeArgs(1,2,))

// Spread syntax (Rest parameters)
const restArgs = function(arg1, arg2, ...restArgs){
  return [arg1, arg2, restArgs]
}

console.log(restArgs(1,2,3,4,5))
console.log(restArgs(1,2))

// Arrow Function
const arrow1 = function (name) {
  return `hello ${name}`
}

// 1. fuction 키워드 생략 가능
const arrow2 = (name) => {
  return `hello ${name}`
}

// 2. 인자가 1개인 경우에만 () 생략 가능
const arrow3 = name => {
  return `hello ${name}`
}

// 3. 함수 body가 return을 포함한 표현식 1개일 경우에 {} , return 삭제 가능
const arrow4 = name => `hello ${name}`


console.log(arrow1('SSAFY'))
console.log(arrow2('SSAFY'))
console.log(arrow3('SSAFY'))
console.log(arrow4('SSAFY'))

// 함수 문맥에서의 this
// const myFunc = function() {
//   console.log(this)
// }
// myFunc()

// const myObj = {
//   numbers: [1],
//   myFunc() {
//     console.log(this)
//     this.numbers.forEach(function (number) {
//       console.log(number)
//       console.log(this)
//     })
//   }
// }
// myObj.myFunc()

console.log('******')
const myObj = {
  numbers: [1],
  myFunc() {
    console.log(this)
    this.numbers.forEach((number) => {
      console.log(number)
      console.log(this)
    })
  }
}
myObj.myFunc()
*/

const colors = ['red','blue','green']
printFunc = function(color) {
  console.log(color)
}

colors.forEach(printFunc)

colors.forEach(function (color) {
  console.log(color)
})

const result = colors.forEach((color, index, array) => {
  console.log(color)
  console.log(index)
  console.log(array)
});

console.log(result)

// map
const numbers = [1,2,3]

// // 함수 정의 (표현식)
// const doubleFunc = function (number) {
//   return number * 2
// }

// // 함수를 다른 함수의 인자로 넣기 (콜백 함수)
// const doubleNumbers = numbers.map(doubleFunc)
// console.log(doubleNumbers)

const doubleNumbers = numbers.map(function (number) {
  return number *2
})
console.log(doubleNumbers)

const products = [
  {name: 'cucumber', type: 'vegetable'},
  {name: 'banana', type: 'fruit'},
  {name: 'carrot', type: 'vegetable'},
  {name: 'apple', type: 'fruit'},

]
const fruitFilter = function (product) {
  return product.type === 'fruit' // true 인 애들만 뽑아서 배열로 만들기
}
const fruits = products.filter(fruitFilter)
console.log(fruits)

const tests = [90,90,70,77]
const sum = tests.reduce(function (total, x) {
  return total + x
}, 0)

const avengers = [
  {name:'Tony Stark', age:45},
  {name:'Steve Rogers', age:32},
  {name:'Thor', age:40},
]

const avenger = avengers.find(function (avenger) {
  return avenger.name === 'Tony Stark'
})
console.log(avenger)

