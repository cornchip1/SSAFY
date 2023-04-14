# Django/DB weekly 

### look up basic format 
```{variable} = {Table}.objects.filter({field_name}__{function} = {value})```

### examples
```articles = Article.objects.filter(title__contains = 'a')```
* Article 의 objects 중에서 title 에 'a' 라는 문자열을 포함한 데이터들만 골라와라

```articles = Article.objects.filter(id__gte = 20)```
* Article objects 중에서 id 가 20보다 큰 것들만 불러와라

복수로 필터 걸기
* AND 조건
  * ```articles = Article.objects.filter(id__gte = 20, id__lt 60)```
  * Article objects 중에서 id가 20보다 크고, 60보다 작은 것들만 불러와라
* multiple filtering
  * & : and
  * | : or
  * ^ : XOR (exclusive or) 두개의 값이 서로 같으면 0, 다르면 1
  * ~ : not 

```articles = Article.objects.filter(title__exact = 'Clock')```
* title 이 정확히 'Clock' 인 데이터만 들고와라

annotate 
* 새로운 필드를 한개 추가했을 때 사용