<template>
  <div class="home">
    <sign-up-sign-in></sign-up-sign-in>
  </div>
</template>

<script>
import SignUpSignIn from "@/components/SignUpSignIn";


export default {
  name: 'Home',
  components: {
    SignUpSignIn
  }
}
</script>
<style lang="scss" scoped>
  .home{
    background: $light-grey;
  }
</style>
