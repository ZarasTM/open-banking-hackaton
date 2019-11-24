<template>
    <div class="container">
        <input v-model="invoiceTitle" placeholder="Invoice title"/>
        <b-row class="padding-lol">
            <b-col>
                <b-row>{{seller.name}}</b-row>
                <b-row>{{seller.address}}</b-row>
                <b-row>{{seller.tin}}</b-row>
                <b-row>{{seller.bankAccount }}</b-row>
            </b-col>
            <b-col>
                <b-row>{{buyer.name}}</b-row>
                <b-row>{{buyer.address}}</b-row>
                <b-row>{{buyer.tin}}</b-row>
                <b-row>{{buyer.bankAccount}}</b-row>
            </b-col>
        </b-row>
        <hr class="my-4">
        <h5>Invoice items</h5>
        <div>
            <invoice-item v-for="item in invoiceItems" :item="item" :enableRemove="true"
                          v-on:remove="invoiceItems.splice(invoiceItems.indexOf(item), 1)"/>
        </div>
        <div class="inner">

            <b-form inline>
                <label class="sr-only" for="inline-form-input-name">Name</label>
                <b-input
                        id="inline-form-input-name"
                        class="mb-2 mr-sm-2 mb-sm-0"
                        v-model="name" placeholder="Item"
                ></b-input>

                <b-input
                        id="inline-form-input-name"
                        class="mb-2 mr-sm-2 mb-sm-0"
                        v-model="quantity" placeholder="Quantity"
                ></b-input>

                <b-input
                        id="inline-form-input-name"
                        class="mb-2 mr-sm-2 mb-sm-0"
                        v-model="unit" placeholder="Unit"
                ></b-input>

                <b-input
                        id="inline-form-input-name"
                        class="mb-2 mr-sm-2 mb-sm-0"
                        v-model="net_ppu" placeholder="Price"
                ></b-input>

                <b-input
                        id="inline-form-input-name"
                        class="mb-2 mr-sm-2 mb-sm-0"
                        v-model="tax_rate" placeholder="Tax rate"
                ></b-input>

                <b-button style="margin-top: 15px;" v-on:click="addItem" variant="primary">Add item</b-button>
            </b-form>
        </div>
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
                    address: 'sss',
                    name: 'sss',
                    tin: 'sss',
                    bankAccount: '213123'
                },
                buyer: {
                    address: 'sss',
                    name: 'aasd',
                    tin: 'asdas',
                    bankAccount: '213123'
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
            async invoice() {
                InvoiceService.createInvoice({
                    seller_nip: this.seller.tin,
                    buyer_nip: this.buyer.tin,
                    title: this.title,
                    currency: this.currency,
                    items: this.invoiceItems
                }).then(response => {
                    console.log(response)
                })
                // InvoiceService.getUserData({ tin: this.seller.tin })
                // InvoiceService.getUserData({ tin: this.buyer.tin })
            }
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
