<template>
    <div v-if="isLoggedIn" class="navbar">
        <div class="nav">
            <h1 class="text-white">YATI</h1>
            <b-link to="/dashboard" router-tag="b-button" active-class="btn-info">
                <v-icon class="v-icon" name="align-justify"/> <span>Dashboard</span></b-link>
            <b-link to="/transactions" router-tag="b-button" active-class="btn-info">
                <v-icon class="v-icon" name="book"/><span>Transactions</span></b-link>
            <b-link to="/invoicing" router-tag="b-button" active-class="btn-info">
                <v-icon class="v-icon" name="file-text"/><span>Invoices</span></b-link>
        </div>
        <b-button @click="logout" block variant="danger"><v-icon class="v-icon" name="log-out"/> Log out</b-button>
    </div>
</template>

<script>
    import HttpService from "@/services/SignInSignUpService";
    export default {
        name: "Navbar",
        computed: {
            isLoggedIn(){
                return this.$store.state.isUserLoggedIn;
            }
        },
        methods: {
            async logout(){
                HttpService.logout().then(resp=>{
                    this.$store.dispatch('logOut');
                    this.$router.push('home');
                });

            }
        }
    }
</script>

<style lang="scss" scoped>
    .navbar {
        margin: 0;
        padding: 12px 15px;
        min-width: $nav-width;
        background: linear-gradient(to bottom, rgb(73, 73, 73) 0%, rgb(56, 56, 56) 100%);
        position: fixed;
        height: 100%;
        overflow: auto;
        z-index: 100;
        display: flex;
        flex-direction: column;
        justify-content: space-between;


        .nav{
            width: 100%;
            display: flex;
            flex-direction: column;
            justify-content: flex-start;
            align-items: flex-start;
        }

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