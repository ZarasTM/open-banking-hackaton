<template>
    <b-jumbotron class="dashboard">
        <template v-slot:header>
            <span class="text-white">Invoicing</span></template>
        <hr class="my-4">
        <b-row>
            <b-form inline>
                <label class="sr-only" for="inline-form-input-name">tin</label>
                <b-input
                        id="inline-form-input-name"
                        class="mb-2 mr-sm-2 mb-sm-0"
                        v-model="tin" placeholder="tin"
                ></b-input>
                <b-button @click="setInvoice" variant="primary">
                    <v-icon class="v-icon" name="edit"/>Create invoice</b-button>
                <b-modal v-model="createInvoice" size="xl" title="Create invoice">
                    <create-invoice/>
                </b-modal>
            </b-form>
        </b-row>

        <b-row>
            <b-form inline>
                <label class="sr-only" for="inline-form-input-name-2">tin</label>
                <b-input
                        id="inline-form-input-name-2"
                        class="mb-2 mr-sm-2 mb-sm-0"
                        v-model="invoiceId" placeholder="Invoice Id"
                ></b-input>
                <b-button @click="getInvoice" variant="primary">
                    <v-icon class="v-icon" name="file-text"/>Display invoice</b-button>
                <b-modal v-model="displayInvoice" size="xl" :title="invoiceId">
                    <display-invoice :invoiceData="currentInvoice" v-on:closeDisplay="closeDisplay"/>
                </b-modal>
            </b-form>
        </b-row>

    </b-jumbotron>
</template>

<script>
    import CreateInvoice from "@/components/CreateInvoice"
    import DisplayInvoice from "@/components/DisplayInvoice"
    import InvoiceService from "@/services/InvoiceService"
    export default {
        name: "Invoicing",
        data: () => {
            return {
                invoiceId: '',
                tin: '',
                displayInvoice: false,
                createInvoice: false,
                currentInvoice: {}
            }
        },
        methods: {
            async setInvoice () {
                this.createInvoice = true;
            },
            async getInvoice () {
                /* TODO: uncomment when endpoint setup
                InvoiceService.getInvoiceData({
                    invoice: this.invoiceId
                }).then(response => {
                    this.currentInvoice = response.data
                    this.displayInvoice = true
                })
                */
                // THIS IS MOCKED
                this.currentInvoice = {
                    seller: {
                        address: 'Address 1',
                        name: 'Name 1',
                        tin: 'tin 1',
                        account_number: '111111111111111'
                    },
                        buyer: {
                        address: 'Address 2',
                        name: 'Name 2',
                        tin: 'tin 2',
                        account_number: '2222222222222222'
                    },
                    amount: '0,00',
                    amount_paid: '0,00',
                    title: 'Title',
                    timestamp: '00-00-00',
                    currency: 'PLN',
                    items: [{
                        name: 'Name 1',
                        quantity: 'Quantity 1',
                        unit: 'Unit 1',
                        net_ppu: 'Net PPU 1',
                        tax_rate: 'Tax rate 1'
                    },
                    {
                        name: 'Name 2',
                        quantity: 'Quantity 2',
                        unit: 'Unit 2',
                        net_ppu: 'Net PPU 2',
                        tax_rate: 'Tax rate 2'
                    },
                    {
                        name: 'Name 3',
                        quantity: 'Quantity 3',
                        unit: 'Unit 3',
                        net_ppu: 'Net PPU 3',
                        tax_rate: 'Tax rate 3'
                    }]
                }
                this.displayInvoice = true;
            },
            closeDisplay: function () {
                this.displayInvoice = false;
                this.currentInvoice = null;
            }
        },
        components: {
            CreateInvoice,
            DisplayInvoice
        }
    }
</script>

<style scoped>

</style>