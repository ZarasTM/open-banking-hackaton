<template>
    <div>
         <create-invoice/>
         <input v-model="invoiceId" placeholder="Invoice Id"/>
         <button v-on:click="displayInvoice">Display invoice</button>
    </div>
    <div v-if="displayInvoice">
        <display-invoice :invoiceData="currentInvoice" v-on:closeDisplay="closeDisplay"/>
    </div>
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
                displayInvoice: false,
                currentInvoice: {}
            }
        },
        methods: {
            async displayInvoice () {
                InvoiceService.getInvoiceData({
                    invoice: this.invoiceId
                }).then(response => {
                    this.currentInvoice = response.data
                    this.displayInvoice = true
                })
            },
            closeDisplay: function () {
                this.displayInvoice = false
                this.currentInvoice = null
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