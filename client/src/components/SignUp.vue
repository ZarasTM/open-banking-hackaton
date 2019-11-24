<template>

    <div>
		<b-form @submit.stop.prevent>
       <b-row>
         <b-col>
            <h4>Register data</h4>
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

           <b-form-group
                   	id="password-confirm-input"
                   	label="Password confirm:"
                   	label-for="input-21"
           >
             <b-form-input
                    id="input-21"
                    type="password"
					v-model="passwordConfirm"
                    required
                    placeholder="Password confirm"
             ></b-form-input>
           </b-form-group>
         </b-col>
         <b-col>
             <h4>Company data</h4>
           <b-form-group
                   	id="company-input"
                   	label="Company name:"
                   	label-for="input-3"
           >
             <b-form-input
                    id="input-3"
                    type="text"
					v-model="company_name"
                    required
                    placeholder="Company name"
             ></b-form-input>
           </b-form-group>

           <b-form-group
                   	id="tin-input"
                   	label="TIN:"
                   	label-for="input-4"
           >
             <b-form-input
                    id="input-4"
                    type="text"
					v-model="tin"
                    required
                    placeholder="TIN"
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
					v-model="address"
                    required
                    placeholder="Address"
             ></b-form-input>
           </b-form-group>

           <b-form-group
                   	id="iban-input"
                   	label="Bank account:"
                   	label-for="input-6"
           >
             <b-form-input
                    id="input-6"
                    type="text"
					v-model="account_number"
                    required
                    placeholder="Account number"
             ></b-form-input>
           </b-form-group>
         </b-col>
    	</b-row>
    </b-form>
	<b-button @click="register" block variant="info">
        <span>Sign Up</span>

	</b-button>
    <b-modal v-model="qrVisible" size="xl" title="QR Code" @ok="closeQR">
        <display-qr :qr="qr" :code="code"/>
    </b-modal>
	</div>
</template>

<script>
	import DisplayQr from "@/components/DisplayQr"
	import HttpService from "@/services/SignInSignUpService"
	import QRCode from 'qrcode'
    export default {
        name: 'SignUp',
        data: () => {
            return {
                email: '',
				password: '',
				passwordConfirm: '',
				company_name: '',
				tin: '',
				address: '',
				account_number: '',
				qr: '',
				code: '',
				qrVisible: false,
				opts: {
      			  	errorCorrectionLevel: 'H',
      			  	type: 'image/jpeg',
      			  	quality: 1,
      			  	margin: 1,
      			  	color: {
      			  	  	dark:"#010599FF",
      			  	  	light:"#FFBF60FF"
      			  	}
      			}
            }
        },
        methods: {
			async register () {
				HttpService.register({
					email: this.email,
					password: this.password,
					company_name: this.company_name,
					tin: this.tin,
					address: this.address,
					account_number: this.account_number
				}).then (response => {
					var that = this
					QRCode.toDataURL(decodeURIComponent(response.data.totp_link), function (err, url) {
						if (err) throw err

  						that.qr = url
					})
					this.code = response.data.totp_secret
					this.qrVisible = true
				})
			},
			async closeQR () {
				this.code = ''
				this.qr = ''
			}
		},
		components: {
			DisplayQr
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
