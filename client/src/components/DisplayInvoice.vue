<template>
<div class="container">
    <b-row>
        <b-col>
            <b-row>{{invoiceData.seller.name}}</b-row>
            <b-row>{{invoiceData.seller.address}}</b-row>
            <b-row>{{invoiceData.seller.tin}}</b-row>
            <b-row>{{invoiceData.seller.account_number }}</b-row>
        </b-col>
        <b-col>
            <b-row>{{invoiceData.buyer.name}}</b-row>
            <b-row>{{invoiceData.buyer.address}}</b-row>
            <b-row>{{invoiceData.buyer.tin}}</b-row>
            <b-row>{{invoiceData.buyer.account_number }}</b-row>
        </b-col>
    </b-row>

    <div class="item-data">
      <span>Items</span>
        <invoice-item v-for="item in invoiceData.items" :item="item" :enableRemove="false"/>
        <span>{{invoiceData.amount}} {{invoiceData.currency}}</span>
        <span>{{invoiceData.amount_paid}} {{invoiceData.currency}}</span>
    </div>
    <div class="invoice-footer">
        <span>{{invoiceData.title}}</span>
        <span>{{invoiceData.timestamp}}</span>
        <button v-on:click="$emit('closeDisplay')">Close</button>
    </div>
  </div>
</template>

<script>
import InvoiceItem from "@/components/InvoiceItem"
export default {
  name: 'DisplayInvoice',
  data: () => {
    return {

    }
  },
  props: {
      invoiceData: Object
  },
  components: {
      InvoiceItem
  }
}
</script>

<style scoped>
</style>
