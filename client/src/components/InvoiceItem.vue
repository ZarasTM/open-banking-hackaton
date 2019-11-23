<template>
  <div>
        <span>{{item.name}}</span>
        <span>{{item.quantity}}</span>
        <span>{{item.unit}}</span>
        <span>{{item.net_ppu}}</span>
        <span>{{item.tax_rate}}</span>
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
