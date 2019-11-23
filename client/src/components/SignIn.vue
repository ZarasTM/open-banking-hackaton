<template>
    <div>
        <b-form @submit="" @reset="">
            <b-form-group
                    id="email-input"
                    label="Email address:"
                    label-for="input-1"
            >
                <b-form-input
                        id="input-1"
                        type="email"
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
                        required
                        placeholder="Password"
                ></b-form-input>
            </b-form-group>


            <b-button type="submit" block variant="info">
                <span>Sign In</span><v-icon class="v-icon" name="log-in"></v-icon></b-button>
        </b-form>
    </div>
</template>

<script>

    export default {
        name: 'SignIn',
        data: () => {
            return {
                email: '',
                pass: ''
            }
        },
        methods: {
            login: function () {
                this.$router.push('dashboard');
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
