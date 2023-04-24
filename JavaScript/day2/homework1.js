// for i in range(1,10,2):
//     print(' '*((9-i)//2),'*'*i,' '*((9-i)//2))


for (let i = 1; i < 10 ; i += 2) {
  result = ' '.repeat((9-i)/2)+'*'.repeat(i)
  console.log(result)
}