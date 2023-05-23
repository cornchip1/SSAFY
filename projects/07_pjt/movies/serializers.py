from rest_framework import serializers
from .models import Actor, Movie, Review


class ActorListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Actor
        fields = '__all__'


class ReviewListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('title', 'content')


class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title', 'overview')

class MovieActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title',)



# 현재 수정중 -> review detail

class ReviewSerializer(serializers.ModelSerializer):
    class MovieReviewSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('title',)
    movie = MovieReviewSerializer(read_only=True)
    
    class Meta:
        model = Review
        fields = '__all__'
        # read_only_fields = ('overview','release_date','poster_path','actors',)

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


    
class MovieSerializer(serializers.ModelSerializer):
    
    class MovieDetailActorSerializer(serializers.ModelSerializer):
        class Meta:
            model = Actor
            fields = ('name',)

    actors = MovieDetailActorSerializer(many=True, read_only=True)

    review_set = ReviewListSerializer(many =True, read_only=True)

    class Meta:
        model = Movie
        fields ='__all__'