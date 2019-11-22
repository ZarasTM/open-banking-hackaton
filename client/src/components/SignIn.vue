<template>
  <div class="container">
    <div class="inner">
      <vnt-header>Sign in</vnt-header>
      <vnt-input v-model="email" placeholder="E-mail"/>
      <vnt-input v-model="pass" type="password" placeholder="Password"/>
    </div>
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
  }
}
</script>

<style scoped>
</style>
