<template>
    <div class="container">
        <img id="qr-code" :src=qr>
        <div>
            <span>{{code}}</span>
        </div>
    </div>
</template>

<script>
export default {
  name: 'DisplayQr',
  data: () => {
    return {
      qr: '',
      opts: {
        errorCorrectionLevel: 'H',
        type: 'image/jpeg',
        quality: 0.3,
        margin: 1,
        color: {
          dark:"#010599FF",
          light:"#FFBF60FF"
        }
      }
    }
  },
  props: {
      code: String,
      qrUrl: String
  },
  methods: {
    async getQRCode () {
      QRCode.toDataURL(this.qrUrl, this.opts, function (err, url) {
        if (err) throw err
 
        this.qr = url
      })
    }
  }
}
</script>

<style scoped>
</style>
