<template>
  <form action="#">
    <div class="form-label-group">
      <input type="email" id="inputEmail" class="form-control" placeholder="Email address" required autofocus>
      <label class="hidden" for="inputEmail">Email address</label>
    </div>

    <div class="form-label-group">
      <input type="password" id="inputPassword" class="form-control" placeholder="Password" required>
      <label class="hidden"  for="inputPassword">Password</label>
    </div>

    <div class="form-label-group">
      <input type="text" id="companyName" class="form-control" placeholder="Company name" required>
      <label class="hidden" for="companyName">Company name</label>
    </div>

    <div class="form-label-group">
      <input type="text" id="nip" class="form-control" placeholder="NIP" required>
      <label class="hidden" for="nip">NIP</label>
    </div>

    <div class="form-label-group">
      <input type="text" id="address" class="form-control" placeholder="Address" required>
      <label class="hidden" for="address">Address</label>
    </div>

    <div class="form-label-group">
      <input type="text" id="iban" class="form-control" placeholder="IBAN" required>
      <label class="hidden" for="iban">IBAN</label>
    </div>

    <div class="form-label-group">
      <input type="text" id="apiKey" class="form-control" placeholder="Api Key" required>
      <label class="hidden" for="apiKey">Api key</label>
    </div>

    <button class="btn  btn-info btn-block" type="submit">Sign Up</button>
  </form>
</template>

<script>

export default {
  name: 'SignUp',
  data: () => {
    return {
      email: '',
      pass: ''
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
