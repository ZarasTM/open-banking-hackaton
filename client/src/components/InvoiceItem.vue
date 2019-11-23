<template>
  <div>
      <b-row style="margin-bottom: 15px;">
          <b-col>{{item.name}}</b-col>
          <b-col>{{item.quantity}}</b-col>
          <b-col>{{item.unit}}</b-col>
          <b-col>{{item.net_ppu}}</b-col>
          <b-col>{{item.tax_rate}}</b-col>
          <b-col v-if="enableRemove">
              <b-button v-on:click="$emit('remove')" variant="danger">Remove</b-button>
          </b-col>
      </b-row>
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
      item: Object,
      enableRemove: Boolean
  }
}
</script>

<style scoped>
</style>
