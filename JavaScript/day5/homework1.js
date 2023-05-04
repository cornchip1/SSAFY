axios.get('https://api.example.com/data')
	.then(function (response) {
	console.log(response.data)
})

/*
동기 함수: 작성 순서대로 먼저 처리하며, 앞의 작업이 다 완료되지 않았으면 뒤에 과정을 시작하지 않음 
비동기 함수: 작성 순서대로 처리를 시작하지만, 작업이 끝난 순서대로 값을 반환함
*/