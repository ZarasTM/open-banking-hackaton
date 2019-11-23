<template>
  <div class="home">
    <sign-up-sign-in></sign-up-sign-in>
  </div>
</template>

<script>
import SignIn from '@/components/SignIn.vue'
import SignUp from "@/components/SignUp";
import SignUpSignIn from "../components/SignUpSignIn";


export default {
  name: 'Home',
  components: {
    SignIn,
    SignUp,
    SignUpSignIn
  }
}
</script>
<style lang="scss" scoped>
  .home{
    background: $light-grey;
  }
</style>
