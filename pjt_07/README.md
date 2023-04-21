# 성용 & 이경의 합작

## Model
* 성용: movies_movie_actors 에서 ManyToManyField 생성할 때 이게 맞나? 했었음
* 이경: 이게 맞았음

## View
* 성용: View 자체는 어려운 게 없었는데, View를 작성하기전에 Serializer 를 구조화를 했어야 한다는 생각이 들었다
* 이경: pdf 를 전체적으로 읽어보고 했었어야 했는데 하나씩 처리하다 보니 나중에 복잡해서 어려웠다. 

## Serializer
* 전체적으로 참조할 때가 어려웠음
* 처음에는 안어렵다고 생각했는데, Serializer 를 분리해야 한다는 걸 나중에 인지해서 프로젝트를 진행하면서 serializer를 추가했고, 그 과정에서 코드가 복잡해짐 (그리고 내 머릿속도 복잡해졌음)
* 초반 구조화의 중요성 인지
* 무지성 many = True 의 폐해
* 이놈이 주범 👇
  ```
    class ReviewSerializer(serializers.ModelSerializer):
        class MovieReviewSerializer(serializers.ModelSerializer):
            class Meta:
                model = Movie
                fields = ('title',)
        movie = MovieReviewSerializer(read_only=True)
        
        class Meta:
            model = Review
            fields = '__all__'
  ```
  * 이유: movie 하나당 여러개의 review가 있는 반면, review는 movie 하나에 엮여있는 구조이기 때문에 정참조이다. 그래서 many = True 를 사용하면 안되는 경우였음 (사용하게 되면 movie is not iterable 오류 발생)
* movie_set -> moives 로 이름을 변경할 때 처음에는 models.py 에서 변경하였으나, to_representation을 사용해서 바꿈
  ```
  class ActorSerializer(serializers.ModelSerializer):
      movie_set = MovieActorSerializer(many = True, read_only = True)

      def to_representation(self, instance):
          rep = super().to_representation(instance)
          rep['movies'] = rep.pop('movie_set',[])
          return rep

      class Meta:
          model = Actor
          fields = '__all__'
          read_only_fields = ('overview',)
  ```