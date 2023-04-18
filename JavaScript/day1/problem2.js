words = ['level', 'noon', 'mom', 'happy', 'ssafy', 'life']

function palindrome(word) {
    // word가 회문인지 아닌지 판별
    let len = word.length
    let result = true
    if (len % 2 == 1 ) {
      for (let i = 0 ; i < len ; i ++ ){
        if (word.charAt(i) != word.charAt(len-(i+1))) {
          // console.log(word.charAt(i), word.slice(-(i+1)))
          result = false
          break
        }
      }
    }
    else {
      for (let i = 0 ; i <= len ; i ++ ){
        if (word.charAt(i) != word.charAt(len-(i+1))) {
          result = false
          break
        }
      }
    }
    return result
  }
  
for (const word of words) {
  console.log(palindrome(word))
}

// 출력 예시
// true
// true
// true
// false
// false
// false
