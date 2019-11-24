<template>
    <b-jumbotron class="dashboard">
        <template v-slot:header>
            <span class="text-white">Invoicing</span></template>
        <hr class="my-4">
        <b-row>
            <b-form inline style="margin-left: 15px;">
                <label class="sr-only" for="inline-form-input-name">tin</label>
                <b-input
                        id="inline-form-input-name"
                        class="mb-2 mr-sm-2 mb-sm-0"
                        v-model="tin" placeholder="tin"
                ></b-input>
                <b-button @click="setInvoice" variant="info">
                    <v-icon class="v-icon" name="edit"/>Create invoice</b-button>
                <b-modal v-model="createInvoice" size="xl" title="Create invoice" @ok="invoice"> 

                    <div class="container">
                        <b-input

                                id="inline-form-input-name"
                                class="mb-2 mr-sm-2 mb-sm-0"
                                v-model="invoiceTitle" placeholder="Invoice title"
                        ></b-input>
                        <b-row class="padding-lol"  style="margin-top: 10px;">
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

                                <b-button v-on:click="addItem" variant="primary">Add item</b-button>
                            </b-form>
                        </div>
                    </div>
                </b-modal>
            </b-form>
        </b-row>

        <b-modal v-model="displayInvoice" size="xl" :title="invoiceId">
            <display-invoice :invoiceData="currentInvoice" v-on:closeDisplay="closeDisplay"/>
        </b-modal>
        <b-card title="Card Title" no-body style="margin-top: 8px;">
            <b-card-header header-tag="nav">
                <b-nav card-header tabs>
                    <b-nav-item :active="inActive"  @click="setIn()">To me</b-nav-item>
                    <b-nav-item :active="!inActive" @click="setOut()">From me</b-nav-item>
                </b-nav>
            </b-card-header>

            <b-card-body class="text-center">
                <b-list-group hover>
                    <b-list-group-item style="cursor: pointer;" hover @click="getInvoice(invoice.invoice_id)" v-for="invoice in invoicesSwitch" class="flex-column align-items-start">
                        <div class="d-flex w-100 justify-content-between">
                            <h5 class="mb-1">{{invoice.title}}</h5>
                            <b-badge variant="info" pill>{{invoice.amount}} {{invoice.currency}}</b-badge>
                        </div>
                    </b-list-group-item>
                </b-list-group>
            </b-card-body>
        </b-card>
    </b-jumbotron>
</template>

<script>
    import CreateInvoice from "@/components/CreateInvoice"
    import DisplayInvoice from "@/components/DisplayInvoice"
    import InvoiceService from "@/services/InvoiceService"
    import InvoiceItem from "@/components/InvoiceItem"
    
    export default {
        name: "Invoicing",
        data: () => {
            return {
                seller: {
                    address: '123',
                    name: '123',
                    tin: '123',
                    bankAccount: '213123'
                },
                buyer: {
                    address: 'sss',
                    name: 'aasd',
                    tin: 'N10P',
                    bankAccount: '213123'
                },
                name: '',
                quantity: '',
                unit: '',
                net_ppu: '',
                tax_rate: '',
                invoiceTitle: '',
                currency: 'PLN',
                invoiceItems: [],

                invoiceId: '',
                tin: '',
                displayInvoice: false,
                createInvoice: false,
                currentInvoice: {},

                invoicesIn: [],
                invoicesOut: [],
                invoicesSwitch: [],
                inActive: false
            }
        },
        methods: {
            async setInvoice () {
                this.createInvoice = true;
            },
            async getInvoice (id) {

                InvoiceService.getInvoiceData({
                    invoice_id: (""+id)
                }).then(response => {
                    this.currentInvoice = response.data;
                    this.displayInvoice = true
                })

                //
                // this.currentInvoice = {
                //     seller: {
                //         address: 'Address 1',
                //         name: 'Name 1',
                //         tin: 'tin 1',
                //         account_number: '111111111111111'
                //     },
                //         buyer: {
                //         address: 'Address 2',
                //         name: 'Name 2',
                //         tin: 'tin 2',
                //         account_number: '2222222222222222'
                //     },
                //     amount: '0,00',
                //     amount_paid: '0,00',
                //     title: 'Title',
                //     timestamp: '00-00-00',
                //     currency: 'PLN',
                //     items: [{
                //         name: 'Name 1',
                //         quantity: 'Quantity 1',
                //         unit: 'Unit 1',
                //         net_ppu: 'Net PPU 1',
                //         tax_rate: 'Tax rate 1'
                //     },
                //     {
                //         name: 'Name 2',
                //         quantity: 'Quantity 2',
                //         unit: 'Unit 2',
                //         net_ppu: 'Net PPU 2',
                //         tax_rate: 'Tax rate 2'
                //     },
                //     {
                //         name: 'Name 3',
                //         quantity: 'Quantity 3',
                //         unit: 'Unit 3',
                //         net_ppu: 'Net PPU 3',
                //         tax_rate: 'Tax rate 3'
                //     }]
                // };
                this.displayInvoice = true;
            },
            closeDisplay: function () {
                this.displayInvoice = false;
                this.currentInvoice = null;
            },
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
                    seller_nip: this.$store.state.user.tin,
                    buyer_nip: this.buyer.tin,
                    title: this.invoiceTitle,
                    currency: this.currency,
                    items: this.invoiceItems
                }).then(response => {
                    console.log(response)
                })
                // InvoiceService.getUserData({ tin: this.seller.tin })
                // InvoiceService.getUserData({ tin: this.buyer.tin })
            },
            setIn: function () {
                this.inActive = true;
                this.invoicesSwitch = this.invoicesIn;
            },
            setOut: function () {
                this.inActive = false;
                this.invoicesSwitch = this.invoicesOut;
            },
        },
        components: {
            CreateInvoice,
            DisplayInvoice,
            InvoiceItem
        },
        beforeCreate: async function () {
            InvoiceService.getInvoicesSummary().then(response => {
                this.invoicesIn = response.data.as_buyer
                this.invoicesOut = response.data.as_seller
                this.invoicesSwitch = this.invoicesOut
            })
        }
    }
</script>

<style >
    .padding-lol{
        padding-left: 15px;
        padding-right: 15px;
    }
    .mb-2{
        width: 185px !important;
    }
</style>