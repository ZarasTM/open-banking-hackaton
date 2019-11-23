<template>
        <b-jumbotron class="dashboard">
            <template v-slot:header>
                <div class="company-name text-white"><v-icon class="v-icon company-icon" name="briefcase"></v-icon>{{companyName}}</div></template>

            <template v-slot:lead>
                <div class="text-white">TIN: {{tin}}</div>
                <div class="text-white">Balance: {{tin}} PLN</div>

            </template>
            <b-button @click="goToTransactions()" variant="info">
                <v-icon class="v-icon" name="book"></v-icon>Transactions</b-button>

            <hr class="my-4">

            <b-list-group>
                <b-list-group-item v-for="company in companies" class="flex-column align-items-start">
                    <div class="d-flex w-100 justify-content-between">
                        <h5 class="mb-1">{{company.name}}</h5>
                        <b-badge class="money-badge" v-if="company.balance>0" variant="info" pill>{{company.balance}} PLN</b-badge>
                        <b-badge class="money-badge" v-else variant="danger" pill>{{company.balance}} PLN</b-badge>
                    </div>

                    <p class="mb-1">
                        TIN: {{company.tin}}
                    </p>

                    <small>{{company.address}}</small>
                </b-list-group-item>
            </b-list-group>
        </b-jumbotron>

</template>

<script>
    export default {
        name: "Dashboard",

        data: ()=>{
            return{
                companyName: 'PolMachniax',
                tin: '12356',
                companies: [
                    {
                        name: 'Budnix',
                        tin: '42069',
                        address: 'ul. Piotrkowska 69',
                        balance: 12345.67
                    },
                    {
                        name: 'Piotreks Sp. Z o.o.',
                        tin: '42069',
                        address: 'ul. Michałowska 420',
                        balance: -12345.67
                    },
                    {
                        name: 'Budnix',
                        tin: '42069',
                        address: 'ul. Piotrkowska 69',
                        balance: 12345.67
                    },
                    {
                        name: 'Piotreks Sp. Z o.o.',
                        tin: '42069',
                        address: 'ul. Michałowska 420',
                        balance: -12345.67
                    },
                    {
                        name: 'Budnix',
                        tin: '42069',
                        address: 'ul. Piotrkowska 69',
                        balance: 12345.67
                    },
                    {
                        name: 'Piotreks Sp. Z o.o.',
                        tin: '42069',
                        address: 'ul. Michałowska 420',
                        balance: -12345.67
                    },
                ]
            }
        },
        methods: {
            goToTransactions: function () {
                this.$router.push('transactions');
            },
        },
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