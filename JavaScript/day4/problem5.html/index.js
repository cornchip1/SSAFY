// 코드를 작성해 주세요
let Score1 = document.getElementById('score1')
let Score2 = document.getElementById('score2')

const result = function(p1,p2){
  dic = {'rock':3 ,'scissors':2 ,'paper':1}
  
  let s1 = Score1.innerText
  let s2 = Score2.innerText

  if ((dic[p1]+1)%3 == (dic[p2]%3)){ 
    s2++
    Score1.textContent = s1
    Score2.textContent = s2

    const modal = document.getElementById('modal')
    modal.addEventListener('click',event => {
      modal.style.display = 'none'
    })
    let modalContent = document.getElementById('modal-content')
    modal.style.display = 'flex'
    modalContent.innerText = 'player 2의 승리입니다!'
  }
  else if ((dic[p1]-1)%3 == (dic[p2]%3)){
    s1++
    Score1.textContent = s1
    Score2.textContent = s2

    const modal = document.getElementById('modal')
    modal.addEventListener('click',event => {
      modal.style.display = 'none'
    })
    let modalContent = document.getElementById('modal-content')
    modal.style.display = 'flex'
    modalContent.innerText = 'player 1의 승리입니다!'
  }
  else if (dic[p1] == (dic[p2]%3)){
    const modal = document.getElementById('modal')
    modal.addEventListener('click',event => {
      modal.style.display = 'none'
    })
    let modalContent = document.getElementById('modal-content')
    modal.style.display = 'flex'
    modalContent.innerText = '무승부입니다!'
  }

}

// 1. 아래 세개 불러오기 
// 2. 버튼 클릭하면 클릭한 걸로 위에있는거 바꾸기
// 3. 오른쪽 이미지 계속 바꾸기 3초동안 랜덤으로 

const section = document.querySelector('section')
lst = ["./img/rock.png","./img/scissors.png","./img/paper.png"]
const p1_choice = document.querySelector('#player1-img')
const p2_choice = document.querySelector('#player2-img')
const scissors = document.querySelector('#scissors-button')
const rock = document.querySelector('#rock-button')
const paper = document.querySelector('#paper-button')

let p1
let p2

scissors.addEventListener('click',function(event){
  p1 = 'scissors'
  p1_choice.src = "./img/scissors.png"
  let r = setInterval(function(){
    const random = Math.floor(Math.random()*3)
    scissors.disabled = true
    rock.disabled = true
    paper.disabled = true
    p2_choice.src = lst[random]
    },100)
    
  setTimeout(() => {
    clearInterval(r) 
    let p2 = document.querySelector('#player2-img')
    if (p2.src.indexOf('scissors') > -1) {
      p2 = 'scissors'}
    else if (p2.src.indexOf('paper') > -1) {
      p2 = 'paper'}
    else if (p2.src.indexOf('rock') > -1) {
      p2 = 'rock'}
    scissors.disabled = false
    rock.disabled = false
    paper.disabled = false

    result(p1,p2)

    },3000)
})

rock.addEventListener('click',function(event){
  p1 = 'rock'
  p1_choice.src = "./img/rock.png"
  let r = setInterval(function(){
    const random = Math.floor(Math.random()*3)
    scissors.disabled = true
    rock.disabled = true
    paper.disabled = true
    p2_choice.src = lst[random]
  },100)
  
  setTimeout(() => {
    clearInterval(r) 
    let p2 = document.querySelector('#player2-img')
    if (p2.src.indexOf('scissors') > -1) {
      p2 = 'scissors'}
    else if (p2.src.indexOf('paper') > -1) {
      p2 = 'paper'}
    else if (p2.src.indexOf('rock') > -1) {
      p2 = 'rock'}
    scissors.disabled = false
    rock.disabled = false
    paper.disabled = false

    result(p1,p2)

    },3000)
})

paper.addEventListener('click',function(event){
  p1 = 'paper'
  p1_choice.src = "./img/paper.png"
  let r = setInterval(function(){
    const random = Math.floor(Math.random()*3)
    scissors.disabled = true
    rock.disabled = true
    paper.disabled = true
    p2_choice.src = lst[random]
  },100)
  
  setTimeout(() => {
    clearInterval(r) 
    let p2 = document.querySelector('#player2-img')
    if (p2.src.indexOf('scissors') > -1) {
      p2 = 'scissors'}
    else if (p2.src.indexOf('paper') > -1) {
      p2 = 'paper'}
    else if (p2.src.indexOf('rock') > -1) {
      p2 = 'rock'}
    scissors.disabled = false
    rock.disabled = false
    paper.disabled = false
    
    result(p1,p2)
    
    },3000)
  
  
})





