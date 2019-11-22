<template>
  <div class="item">
        <span>{{item.name}}</span>
        <span>{{item.amount}}</span>
        <span>{{item.price}}</span>
        <span>{{item.taxRate}}</span>
        <button v-on:click="$emit('remove')">Remove</button>
  </div>
</template>

<script>
export default {
  name: 'InvoiceItem',
  data: () => {
    return {

    }
  },
  props: {
      item: Object
  }
}
</script>

<style scoped>
</style>
