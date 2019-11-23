<template>
    <div class="navbar">
        <b-link to="/dashboard" router-tag="b-button" active-class="btn-info">
             <v-icon class="v-icon" name="align-justify"/> <span>Dashboard</span></b-link>
        <b-link to="/transactions" router-tag="b-button" active-class="btn-info">
            <v-icon class="v-icon" name="book"/><span>Transactions</span></b-link>
        <b-link to="/invoicing" router-tag="b-button" active-class="btn-info">
            <v-icon class="v-icon" name="file-text"/><span>Invoices</span></b-link>
    </div>
</template>

<script>
    export default {
        name: "Navbar"
    }
</script>

<style lang="scss" scoped>
    .navbar {
        margin: 0;
        padding: 50px 15px;
        min-width: $nav-width;
        background-color: $dark-grey;
        position: fixed;
        height: 100%;
        overflow: auto;
        z-index: 100;
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
        align-items: flex-start;

        .btn{
            width: 100%;
            margin-bottom: 5px;
        }

        button{
            display: flex !important;
        }

        .v-icon{
            margin-right: 5px;
        }
    }

</style>