<template>
    <b-jumbotron class="dashboard">
        <template v-slot:header>
            <span class="text-white">Transactions</span></template>
        <hr class="my-4">
        <b-card title="Card Title" no-body>
            <b-card-header header-tag="nav">
                <b-nav card-header tabs>
                    <b-nav-item :active="inActive" @click="setIn()">In transactions</b-nav-item>
                    <b-nav-item :active="!inActive" @click="setOut()">Out transactions</b-nav-item>
                </b-nav>
            </b-card-header>

            <b-card-body class="text-center">
                <b-list-group>
                    <b-list-group-item v-for="transaction in transactions" class="flex-column align-items-start">
                        <div class="d-flex w-100 justify-content-between">
                            <h5 class="mb-1">{{transaction.title}}</h5>
                            <b-badge v-if="transactions===inTransactions" variant="info" pill>{{transaction.amount}}
                                {{transaction.currency}}
                            </b-badge>
                            <b-badge v-else variant="danger" pill>{{transaction.amount}} {{transaction.currency}}
                            </b-badge>
                        </div>
                        <p class="mb-1 text-left">
                            {{transaction.other_party}}
                        </p>
                    </b-list-group-item>
                </b-list-group>
            </b-card-body>
        </b-card>

    </b-jumbotron>

</template>

<script>
    import TransactionService from "../services/TransactionService";

    export default {
        name: "Transactions",
        data: () => {
            return {
                inActive: false,
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
                transactions: [],
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
            TransactionService.getTransactionsSummary().then(response => {
                this.inTransactions = response.data.as_buyer
                this.outTransactions = response.data.as_seller
                this.transactions = this.outTransactions
            })

        }
    }
</script>

<style scoped>

</style>