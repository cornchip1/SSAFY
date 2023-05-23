<template>
  
    <div class="card" >
        <img :src="imageUrl" class="card-img-top" alt="...">
        <div class="card-body">
        <h5 class="card-title text-center fw-bold">{{movie.title}}</h5>
        <p class="card-text">{{movie.overview}}</p>
      </div>
    </div>

</template>

<script>
export default {
  name:"MovieCard",
  props: {
    movie:Object
  },
  data(){
    return {
      imageUrl : `https://image.tmdb.org/t/p/original/${this.movie.poster_path}`
    }
  }

}
</script>

<style>
.card-text {
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-line-clamp: 3;
    overflow: hidden;
    text-overflow: ellipsis;
  }
</style>