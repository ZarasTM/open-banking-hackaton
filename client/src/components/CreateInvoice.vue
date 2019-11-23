<template>
  <div class="container">
    <div class="company-data">
        <div>
            <span>{{seller.name}}</span>
            <span>{{seller.address}}</span>
            <span>{{seller.nip}}</span>
            <span>{{seller.bankAccount}}</span>
        </div>
        <div>
            <span>{{buyer.name}}</span>
            <span>{{buyer.address}}</span>
            <span>{{buyer.nip}}</span>
            <span>{{buyer.bankAccount}}</span>
        </div>
    </div>
    <div class="inner">
      <span>Invoice items</span>
      <div>
        <input v-model="name" placeholder="Item"/>
        <input v-model="quantity" placeholder="Quantity"/>
        <input v-model="unit" placeholder="Unit"/>
        <input v-model="net_ppu" placeholder="Price"/>
        <input v-model="tax_rate" placeholder="Tax rate"/>
        <button v-on:click="addItem">Add item</button>
      </div>
    </div>
    <div>
        <invoice-item v-for="item in invoiceItems" :item="item" :enableRemove="true" v-on:remove="invoiceItems.splice(invoiceItems.indexOf(item), 1)"/>
    </div>
    <input v-model="invoiceTitle" placeholder="Invoice title"/>
    <button>Invoice</button>
  </div>
</template>

<script>
import InvoiceItem from "@/components/InvoiceItem"
import InvoiceService from "@/services/InvoiceService"

export default {
  name: 'CreateInvoice',
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
        quantity: '',
        unit: '',
        net_ppu: '',
        tax_rate: '',
        invoiceTitle: '',
        currency: 'PLN',
        invoiceItems: []
    }
  },
  methods: {
      addItem: function () {
        this.invoiceItems.push({
            name: this.name,
            quantity: parseInt(this.quantity),
            unit: this.unit,
            net_ppu: parseInt(this.net_ppu),
            tax_rate: parseInt(this.tax_rate)
        })
        this.name = ''
        this.quantity = ''
        this.unit = ''
        this.net_ppu = ''
        this.tax_rate = ''
      },
      async invoice () {
        console.log({
          seller_nip: this.seller.nip,
          buyer_nip: this.buyer.nip,
          title: this.title,
          currency: this.currency,
          items: this.invoiceItems
        })
        InvoiceService.createInvoice({
          seller_nip: this.seller.nip,
          buyer_nip: this.buyer.nip,
          title: this.title,
          currency: this.currency,
          items: this.invoiceItems
        }).then (response => {
          console.log(response)
        })
          // InvoiceService.getUserData({ tin: this.seller.nip })
          // InvoiceService.getUserData({ tin: this.buyer.nip })
      }
  },
  components: {
      InvoiceItem
  }
}
</script>

<style scoped>
</style>
