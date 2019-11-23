<template>
    <div>
         <create-invoice/>
    </div>
</template>

<script>
    import CreateInvoice from "@/components/CreateInvoice"
    export default {
        name: "Dashboard",
        components: {
            CreateInvoice
        }
    }
</script>

<style scoped>

</style>