<template>
    <div>
        <b-form @submit.stop.prevent>
            <h4>Login data</h4>
            <b-form-group
                    id="email-input"
                    label="Email address:"
                    label-for="input-1"
            >
                <b-form-input
                        id="input-1"
                        type="email"
                        v-model="email"
                        required
                        placeholder="Enter email"
                ></b-form-input>
            </b-form-group>

            <b-form-group
                    id="password-input"
                    label="Password:"
                    label-for="input-2"
            >
                <b-form-input
                        id="input-2"
                        type="password"
                        v-model="password"
                        required
                        placeholder="Password"
                ></b-form-input>
            </b-form-group>

            <b-form-checkbox
                    id="checkbox-1"
                    name="checkbox-1"
                    v-model="remember"
            >
                Remember
            </b-form-checkbox>

            <b-button @click="showAuthCodeModal" block variant="info" style="margin-top: 10px;">
                <span>Sign In</span>
                <v-icon class="v-icon" name="log-in"></v-icon>
            </b-button>
        </b-form>

        <b-modal v-model="isAuthCodeModalVisible" title="Enter auth code" @ok="login">
            <b-form @submit.stop.prevent>
                <b-form-group
                        id="auth-input"
                        label="Authentication code:"
                        label-for="input-3"
                >
                    <b-form-input
                            id="input-3"
                            type="text"
                            v-model="totp_code"
                            required
                            placeholder="Authentication code"
                    ></b-form-input>
                </b-form-group>
            </b-form>
        </b-modal>
    </div>
</template>

<script>
    import HttpService from "@/services/SignInSignUpService"

    export default {
        name: 'SignIn',
        data: () => {
            return {
                email: '',
                password: '',
                totp_code: '',
                remember: false,
                isAuthCodeModalVisible: false,
            }
        },
        methods: {
            async login() {
                HttpService.login({
                    email: this.email,
                    password: this.password,
                    remember: this.remember,
                    totp_code: this.totp_code
                }).then(response => {
                    if (response.status == 200) {

                        HttpService.tokenValid().then(response => {
                            console.log(response)
                        }).catch(error => {
                            HttpService.generateToken().then(response => {
                                open(response.data.oauth_link, '_blank')
                            })
                            return
                        })

                        this.$store.dispatch('logIn');
                        this.$router.push('dashboard');
                    }
                })
            },
            showAuthCodeModal: function () {
                this.isAuthCodeModalVisible = true;
            }
        }
    }
</script>

<style scoped lang="scss">
    .hidden {
        visibility: hidden;
    }

    .btn-google {
        color: white;
        background-color: #ea4335;
    }

    .btn-facebook {
        color: white;
        background-color: #3b5998;
    }
</style>
