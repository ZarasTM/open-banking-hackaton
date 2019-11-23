<template>
  <div id="app">
    <navbar/>
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
  background: linear-gradient(to bottom, rgb(114, 113, 113) 0%, rgb(78, 78, 78) 100%);
  
}

.jumbotron{
  margin-bottom: 0 !important;
}

.btn-default{
  background-color: #68889E;
  color:#FFF;
  border-color: #2F3E48;
}

</style>

#185598
#59B896