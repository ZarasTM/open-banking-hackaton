<template>
  <div class="home">
    <SignIn/>
    <CreateInvoice/>
  </div>
</template>

<script>
import SignIn from '@/components/SignIn.vue'
import CreateInvoice from '@/components/CreateInvoice.vue'

export default {
  name: 'Home',
  components: {
    SignIn,
    CreateInvoice
  }
}
</script>
