<template>
  <div>
    <h1>Top Rated Movies</h1>
    <div class="container">
      <div class="row row-cols-2 row-cols-sm-3 row-cols-md-4 g-2  d-flex justify-content-center">
        <MovieCard
          v-for = "movie in movies" 
          :key = "movie.id"
          :movie = "movie"
          class="mx-3"
        />
      </div>
    </div>
  </div>
</template>

<script>
const MOVIE_API_KEY = "eb6632a590213714114bb61c304b7e9c"
import MovieCard from "@/components/MovieCard.vue"
import axios from "axios"
export default {
  name:"MovieView",
  components : {
    MovieCard
  },
  data () {
    return {
      movies:null
    }
  },
  created(){
    this.getMovieList()
  },
  methods:{
    getMovieList(){
      const movieUrl = `https://api.themoviedb.org/3/movie/top_rated?api_key=${MOVIE_API_KEY}&language=en-US&page=1`
      axios({
        methods : "get",
        url : movieUrl
      })
      .then(response => {
        const movies = response.data.results
        this.movies = movies
      })
      .catch(err=>{
        console.log(err)
      })
    }
  }
}
</script>

<style>

</style>