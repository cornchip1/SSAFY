# Django/DB weekly 

### basic format 
```{variable} = {Table}.objects.filter({field_name}__{function} = {value})```

### examples
```articles = Article.objects.filter(title__contains = 'a')```
* Article 의 objects 중에서 title 에 'a' 라는 문자열을 포함한 데이터들만 골라와라

```articles = Article.objects.filter(id__gte = 20)```
* Article objects 중에서 id 가 20보다 큰 것들만 불러와라

```articles = Article.objects.filter(id__gte = 20 and id__(smaller than) 60)```
* 가능한가?

```articles = Article.objects.filter(title__exact = 'Clock')```
* title 이 정확히 'Clock' 인 데이터만 들고와라