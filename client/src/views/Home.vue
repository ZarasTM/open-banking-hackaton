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
      if (response.status === 200) {

        HttpService.tokenValid().then(response => {
          console.log(response)
        }).catch(error => {
          HttpService.generateToken().then(response => {
            open(response.data.oauth_link, '_blank')
          })
          return
        })
          this.$store.dispatch('logIn');
        this.$router.push('dashboard');

      }
    })
  }
}
</script>
<style lang="scss" scoped>
  .home{
    padding-left: -($nav-width+50px);
  }
</style>
