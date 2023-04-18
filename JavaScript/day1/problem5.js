const participantNums =  [[1, 3, 2, 2, 1], 
[3, 7, 100, 21, 13, 6, 5, 7, 5, 6, 3, 13, 21],
[9, 1, 8, 7, 71, 33, 62, 35, 11, 4, 7, 71, 33, 8, 9, 1, 4, 11, 35]
]

// 3
// 100
// 62

// 같은 값이 없는 친구를 반환한다
for (c of participantNums) {

  // particpiantNums 를 하나씩 쪼개서
  for (i of c) {
    // 만약 c 에서 2개 이상 있다면
    if (c.filter( element => element == i).length > 1) {
      // pass
    } 
    // c 에서 1개밖에 없으면 print
    else {
      console.log(i)
    }
  }
}