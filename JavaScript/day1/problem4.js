const p1 = ['rock', 'paper', 'scissors', 'scissors', 'rock', 'rock', 'paper', 'paper', 'rock', 'scissors']
const p2 = ['paper', 'paper', 'rock', 'scissors', 'paper', 'scissors', 'scissors', 'rock', 'rock', 'rock']

const dic = {'rock':3,'scissors':2,'paper':1}

for (let i = 0; i < p1.length ; i ++){
  let p1_choice = dic[p1[i]]
  let p2_choice = dic[p2[i]]
  // console.log(p1_choice,p2_choice)
  if (p1_choice == p2_choice) {
    // 같은 거 냈을 때
    console.log(0)
  }
  else if ((p1_choice + 1)%3 == p2_choice%3) {
    // 2가 이겼을 때
    console.log(2)
  }
  
  else if ((p2_choice + 1) %3 == p1_choice%3){
    console.log(1)
  }

}

