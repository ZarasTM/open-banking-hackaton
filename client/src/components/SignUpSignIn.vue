<template>
    <div class="container">
        <div class="row">
            <div class=" col-md-9 col-lg-9 mx-auto">
                <div class="card my-5">
                    <div class="btn-group card-header" role="group">
                        <button
                                v-for="tab in tabs"
                                :key="tab"
                                :class="['btn', { 'btn-info': activeTab === tab },{ 'btn-secondary': activeTab !== tab }]"
                                @click="activeTab = tab"
                        >Sign {{ tab }}</button>
                    </div>
                    <div class="card-body">
                        <keep-alive>
                            <component v-bind:is="formComponent"></component>
                        </keep-alive>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import SignUp from "./SignUp";
    import SignIn from "./SignIn";

    export default {
        name: "SignUpSignIn",
        components: {
            SignUp,
            SignIn
        },
        data: () => {
            return {
                activeTab: 'In',
                tabs: ['Up', 'In']
            }
        },
        computed: {
            formComponent: function () {
                return 'sign-'+this.activeTab;
            }
        }
    }
</script>

<style scoped>
</style>