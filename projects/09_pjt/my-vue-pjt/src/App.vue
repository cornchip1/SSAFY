<template>
  <div id="app">
    <nav class="navbar navbar-expand-md" style="background-color: #e3f2fd;">
      <div class="container-fluid">
        <router-link class="navbar-brand" :to="{name:'MovieView'}" >
          <img src="@/assets/SSAFY.png" alt=""  width="40" height="40">
        </router-link>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse justify-content-end" id="navbarNav">
          <ul class="navbar-nav">
            <li class="nav-item">
              <router-link :class="{'nav-link': true, 'active': $route.name === 'MovieView'}" :to="{name:'MovieView'}">Movie</router-link>
            </li>
            <li class="nav-item">
              <router-link :class="{'nav-link': true, 'active': $route.name === 'RandomView'}" :to="{name:'RandomView'}">Random</router-link>
            </li>
            <li class="nav-item">
              <router-link :class="{'nav-link': true, 'active': $route.name === 'WatchListView'}" :to="{name:'WatchListView'}">Watch List</router-link>            
            </li>
          </ul>
        </div>
      </div>
    </nav>
    <router-view id="router-view"/>

  </div>
</template>

<style>
#router-view {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}


</style>
