<template>

    <b-form @submit="" @reset="" >
       <b-row>
         <b-col>

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

           <b-form-group
                   id="password-confirm-input"
                   label="Password confirm:"
                   label-for="input-21"
           >
             <b-form-input
                     id="input-21"
                     type="password"
                     required
                     placeholder="Password confirm"
             ></b-form-input>
           </b-form-group>

           <b-form-group
                   id="api-input"
                   label="Api Key:"
                   label-for="input-7"
           >
             <b-form-input
                     id="input-7"
                     type="text"
                     required
                     placeholder="Api key"
             ></b-form-input>
           </b-form-group>
         </b-col>
         <b-col>
           <b-form-group
                   id="company-input"
                   label="Company name:"
                   label-for="input-3"
           >
             <b-form-input
                     id="input-3"
                     type="text"
                     required
                     placeholder="Company name"
             ></b-form-input>
           </b-form-group>

           <b-form-group
                   id="nip-input"
                   label="NIP:"
                   label-for="input-4"
           >
             <b-form-input
                     id="input-4"
                     type="text"
                     required
                     placeholder="NIP"
             ></b-form-input>
           </b-form-group>

           <b-form-group
                   id="address-input"
                   label="Address:"
                   label-for="input-5"
           >
             <b-form-input
                     id="input-5"
                     type="text"
                     required
                     placeholder="Address"
             ></b-form-input>
           </b-form-group>

           <b-form-group
                   id="iban-input"
                   label="IBAN:"
                   label-for="input-6"
           >
             <b-form-input
                     id="input-6"
                     type="text"
                     required
                     placeholder="IBAN"
             ></b-form-input>
           </b-form-group>
         </b-col>
       </b-row>
        <b-button type="submit" block variant="info">
            <span>Sign Up</span><v-icon class="v-icon" name="chevron-up"></v-icon></b-button>
    </b-form>
</template>

<script>

    export default {
        name: 'SignUp',
        data: () => {
            return {
                email: '',
                pass: ''
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
