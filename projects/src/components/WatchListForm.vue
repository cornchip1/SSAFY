<template>
  <div>
    <form @submit.prevent> 
      <input v-model.trim = "input" type="text">
      <input @click="AddToItems" type="submit">
    </form>
    <WatchListItem
      :watch-list = "watchList"
      @updateWatchList = "updateWatchList"
      />
  </div>
</template>

<script>
import WatchListItem from './WatchListItem.vue'

export default {
  name : "WatchListForm",
  components :{
    WatchListItem
    },
  data(){
    return {
      input: '',
      watchList : [],
      watched: false
    }
  },
  methods: {
    AddToItems(){
      if (this.input === ''){
        alert('내용을 입력하세요!')
      }
      else{
        const watchItem = {
          title: this.input,
          watched: this.watched
        }
        this.watchList.push(watchItem)
      }
      this.input = ''
    },
    updateWatchList(idx) {
      this.watchList[idx].watched = !this.watchList[idx].watched
    }
  }
}
</script>

<style>

</style>