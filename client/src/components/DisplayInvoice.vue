<template>
<div class="container">
    <h1>Invoice: {{invoiceData.title}}</h1>
    <h2>{{invoiceData.timestamp}}</h2>
    <b-row class="padding-lol">
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
    <hr class="my-4">
    <div class="item-data">
      <h2>Items</h2>
<!--        <invoice-item v-for="item in invoiceData.items" :item="item" :enableRemove="false"/>-->
        <b-table striped :items="invoiceData.items"></b-table>
        <h4>Total: {{invoiceData.amount}} {{invoiceData.currency}}</h4>
        <h4>Already paid: {{invoiceData.amount_paid}} {{invoiceData.currency}}</h4>
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
    .padding-lol{
        padding-left: 15px;
        padding-right: 15px;
    }
</style>
