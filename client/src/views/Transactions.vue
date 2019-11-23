<template>
    <b-jumbotron class="dashboard">
        <template v-slot:header>
            Transactions</template>

        <b-card title="Card Title" no-body>
            <b-card-header header-tag="nav">
                <b-nav card-header tabs>
                    <b-nav-item :active="inActive"  @click="setIn()">In transaction</b-nav-item>
                    <b-nav-item  :active="!inActive" @click="setOut()">Out transaction</b-nav-item>
                </b-nav>
            </b-card-header>

            <b-card-body class="text-center">
                <b-list-group>
                    <b-list-group-item v-for="transaction in transactions" class="flex-column align-items-start">
                        <div class="d-flex w-100 justify-content-between">
                            <h5 class="mb-1">{{transaction.name}}</h5>
                            <b-badge variant="info" pill>{{transaction.amount}} PLN</b-badge>
                        </div>
                    </b-list-group-item>
                </b-list-group>
            </b-card-body>
        </b-card>

    </b-jumbotron>

</template>

<script>
    export default {
        name: "Transactions",
        data: ()=>{
            return{
                inActive: true,
                inTransactions: [
                    {
                        name: 'InTransaction 01',
                        amount: 12345.67
                    },
                    {
                        name: 'InTransaction 02',
                        amount: 12345.67
                    },
                ],
                outTransactions: [
                    {
                        name: 'Out Transaction 01',
                        amount: 12345.67
                    },
                    {
                        name: 'Out Transaction 031231',
                        amount: 12345.67
                    },
                    {
                        name: 'Out Transaction 01231',
                        amount: 12345.67
                    },
                ],
                transactions: [
                ],
            }
        },
        methods: {
            setIn: function () {
                this.inActive = true;
                this.transactions = this.inTransactions;
            },
            setOut: function () {
                this.inActive = false;
                this.transactions = this.outTransactions;
            },
        },
        created() {
            this.transactions = this.inTransactions
        }
    }
</script>

<style scoped>

</style>