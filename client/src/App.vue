<template>
  <div id="app">
    <navbar v-if=""/>
    <router-view class="router"/>
  </div>
</template>
<script>
  import Navbar from "./components/Navbar";
  export default {
    components: {Navbar}
  }
</script>
<style lang="scss">
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}


.router {
  @extend %full-page;
  padding-top: 100px;
  padding-left: $nav-width+50px;
  position: absolute;
  top: 0;
  background: $light-grey;
}
  .jumbotron{
    margin-bottom: 0 !important;
  }

</style>
