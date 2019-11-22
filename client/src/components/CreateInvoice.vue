<template>
  <div class="container">
    <div class="company-data">
        <!-- TDOD: Repair "legacy" code xD -->
        <vnt-header>
            <span slot="header">{{seller.name}}</span>
            <span slot="subheader">{{seller.address}}</span>
            <span slot="subheader">{{seller.nip}}</span>
        </vnt-header>
        <vnt-header>
            <span slot="header">{{buyer.name}}</span>
            <span slot="subheader">{{buyer.address}}</span>
            <span slot="subheader">{{buyer.nip}}</span>
        </vnt-header>
    </div>
    <div class="inner">
      <vnt-header>Invoice items</vnt-header>
      <div>
        <input v-model="name" placeholder="Item"/>
        <input v-model="amount" placeholder="Amount"/>
        <input v-model="price" placeholder="Price"/>
        <input v-model="taxRate" placeholder="Tax rate"/>
        <button v-on:click="addItem">Add item</button>
      </div>
    </div>
    <div>
        <invoice-item v-for="item in invoiceItems" :item="item" v-on:remove="invoiceItems.splice(invoiceItems.indexOf(item), 1)"/>
    </div>
    <input v-model="invoiceTitle" placeholder="Invoice title"/>
    <button v-on:click="invoice">Invoice</button>
  </div>
</template>

<script>
import InvoiceItem from "./InvoiceItem"
export default {
  name: 'SignIn',
  data: () => {
    return {
        seller: {
            address: '',
            name: '',
            nip: ''
        },
        buyer: {
            address: '',
            name: '',
            nip: ''
        },
        name: '',
        amount: '',
        price: '',
        taxRate: '',
        invoiceTitle: '',
        invoiceItems: []
    }
  },
  methods: {
      addItem: function () {
        this.invoiceItems.push({
            name: this.name,
            amount: this.amount,
            price: this.price,
            taxRate: this.taxRate
        })
        this.name = ''
        this.amount = ''
        this.price = ''
        this.taxRate = ''
      },
      invoice: function () {
          console.log("Invoiced with: ")
          console.log(this.invoiceItems)
          console.log(this.invoiceTitle)
      }
  },
  components: {
      InvoiceItem
  }
}
</script>

<style scoped>
</style>
