function repeat(strvalue,times){
  let result = strvalue.repeat(times);
  console.log(result);
}

for (let i = 0 ; i < 6 ; i ++) {
  repeat('*',i)
}
