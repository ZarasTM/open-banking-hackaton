<template>
  <div class="home">
    <sign-up-sign-in></sign-up-sign-in>
  </div>
</template>

<script>
import SignUpSignIn from "@/components/SignUpSignIn";
import HttpService from "@/services/SignInSignUpService"


export default {
  name: 'Home',
  components: {
    SignUpSignIn
  },
  beforeCreate: async function () {
    HttpService.isLogged().then((response) => {
      console.log(response.status
      );
      if (response.status === 200) {
        this.$store.dispatch('logIn');
        this.$router.push('dashboard');
      } else {
        console.log('');
      }
    });
  }
}
</script>
<style lang="scss" scoped>
  .home{
    padding-left: -($nav-width+50px);
  }
</style>
