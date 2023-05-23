<template>
  <div>
    <div v-if="weather">
      <h1>{{ weather }} 한 날씨에 이런 영화 어때요?</h1>
    </div>
    <div v-if="!weather">
      <h1>날씨 업데이트 중...</h1>
    </div>
    <button @click="getMovieList" class="btn btn-success mb-2" style="width: 18rem;">Pick</button>
      <div class="card" style="width: 18rem;">
        <img :src="imageUrl" class="card-img-top" alt="...">
        <div class="card-body">
        <h5 class="card-title text-center fw-bold">{{movie.title}}</h5>
        <p class="card-text">{{movie.overview}}</p>
      </div>
    </div>
  </div>
</template>

<script>
const MOVIE_API_KEY = "eb6632a590213714114bb61c304b7e9c"
const WEATHER_API_KEY = "a605f8a4dbd60deadcf2fd220963bf32"
import axios from "axios"
import _ from 'lodash'

export default {
  name:"RandomView",
  data() {
    return {
      movie: '',
      imageUrl : null,
      weather : '',

    }
  },
  created(){
    this.getMovieList()
    this.getWeather()
  },
  methods: {
    getMovieList(){
      const movieUrl = `https://api.themoviedb.org/3/movie/top_rated?api_key=${MOVIE_API_KEY}&language=en-US&page=1`
      axios({
        methods : "get",
        url : movieUrl
      })
      .then(response => {
        const movies = response.data.results
        this.movie = _.sample(movies)
        this.imageUrl = `https://image.tmdb.org/t/p/original/${this.movie.poster_path}`
      })
      .catch(err=>{
        console.log(err)
      })
    },
    getWeather(){
      const weatherUrl = `https://api.openweathermap.org/data/2.5/weather?q=Seoul&appid=${WEATHER_API_KEY}`
      axios({
        method: 'get',
        url: weatherUrl
      })
      .then(res=>{
        this.weather = res.data.weather[0].description

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