<template>
  <div>
    <ul class="list-group">
      <li 
        v-for="(m,idx) in watchList" 
        :key="idx" 
        @click="isWatched(idx)" 
        :class="{ 
          'watched': m.watched,
          'list-group-item' :  true,
          'list-group-item-light' : !m.watched,
          'list-group-item-dark' : m.watched ,
          }"
      >{{m.title}}</li>
    </ul>
  </div>
</template>

<script>
export default {
  name : "WatchListItem",

  props:{
    watchList:Array
  },
  data(){
    return {
      design : "list-group-item list-group-item-light"
    }
  },
  methods: {
    isWatched(idx) {
      // this.watchList[idx].watched = !this.watchList[idx].watched
      // console.log(this.watchList[idx])
      this.$emit("updateWatchList", idx)
      
    }

  }
}
</script>

<style>
  .watched {
    text-decoration: line-through;
  }
  
</style>