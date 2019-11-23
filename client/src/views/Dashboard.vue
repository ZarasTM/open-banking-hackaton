<template>
        <b-jumbotron class="dashboard">
            <template v-slot:header>
                <div class="company-name text-white"><v-icon class="v-icon company-icon" name="briefcase"></v-icon>{{companyName}}</div></template>

            <template v-slot:lead>
                <div class="text-white">TIN: {{tin}}</div>
                <div class="text-white">Balance: {{balance}} PLN</div>

            </template>
            <b-button @click="goToTransactions()" variant="info">
                <v-icon class="v-icon" name="book"></v-icon>Transactions</b-button>

            <hr class="my-4">

            <b-list-group>
                <b-list-group-item v-for="company in companies" class="flex-column align-items-start">
                    <div class="d-flex w-100 justify-content-between">
                        <h5 class="mb-1">{{company.balance_user.name}}</h5>
                        <b-badge class="money-badge" v-if="company.amount>0" variant="info" pill>{{company.amount}} {{company.currency}}</b-badge>
                        <b-badge class="money-badge" v-else variant="danger" pill>{{company.amount}} PLN</b-badge>
                    </div>

                    <p class="mb-1">
                        TIN: {{company.balance_user.tin}}
                    </p>

                    <small>{{company.balance_user.address}}</small>
                </b-list-group-item>
            </b-list-group>
        </b-jumbotron>

</template>

<script>
    import DashboardService from "@/services/DashboardService"
    export default {
        name: "Dashboard",
        data: () => {
            return {
                companyName: '',
                tin: '',
                balance: '',
                companies: []
            }
        },
        methods: {
            goToTransactions: function () {
                this.$router.push('transactions');
            },
            calculateBalance(){
                let balance = 0
                this.companies.forEach(function (company) {
                    console.log(company.amount)
                    balance += company.amount
                })
                this.balance = balance
            }
        },
        beforeCreate: async function () {
            DashboardService.fetchUserData().then((response) => {
                this.companyName = response.data.user_inv_data.name
                this.tin = response.data.user_inv_data.tin
                this.companies = response.data.balances
                const user = {
                    name: response.data.user_inv_data.name,
                    address: response.data.user_inv_data.address,
                    tin: response.data.user_inv_data.tin,
                    account_number: response.data.user_inv_data.account_number
                }
                this.$store.dispatch('setUser', user)
                this.calculateBalance()
            });
        }
    }

</script>

<style scoped>
    .company-name{
        display: flex;
    }
    .company-icon{
        width: 3.5rem;
    }
</style>