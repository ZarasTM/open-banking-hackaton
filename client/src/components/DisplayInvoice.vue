<template>
<div class="container">
    <div class="company-data">
        <div>
            <span>{{invoiceData.seller.name}}</span>
            <span>{{invoiceData.seller.address}}</span>
            <span>{{invoiceData.seller.tin}}</span>
            <span>{{invoiceData.seller.account_number }}</span>
        </div>
        <div>
            <span>{{invoiceData.buyer.name}}</span>
            <span>{{invoiceData.buyer.address}}</span>
            <span>{{invoiceData.buyer.tin}}</span>
            <span>{{invoiceData.buyer.account_number}}</span>
        </div>
    </div>
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
