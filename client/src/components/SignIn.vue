<template>
  <div>
    <form action="#">
      <div class="form-label-group">
        <input type="email" id="inputEmail" class="form-control" placeholder="Email address" required autofocus>
        <label class="hidden" for="inputEmail">Email address</label>
      </div>

      <div class="form-label-group">
        <input type="password" id="inputPassword" class="form-control" placeholder="Password" required>
        <label class="hidden"  for="inputPassword">Password</label>
      </div>

      <div class="custom-control custom-checkbox mb-3">
        <input type="checkbox" class="custom-control-input" id="customCheck1">
        <label class="custom-control-label" for="customCheck1">Remember password</label>
      </div>
    </form>
    <button @click="login" class="btn  btn-info btn-block" type="submit">Sign In</button>
  </div>
</template>

<script>

export default {
  name: 'SignIn',
  data: () => {
    return {
      email: '',
      pass: ''
    }
  },
  methods: {
    login: function(){
      this.$router.push('dashboard');
    }
  }
}
</script>

<style scoped lang="scss">
  .hidden {
    visibility: hidden;
  }
  .btn-google {
    color: white;
    background-color: #ea4335;
  }

  .btn-facebook {
    color: white;
    background-color: #3b5998;
  }
</style>
