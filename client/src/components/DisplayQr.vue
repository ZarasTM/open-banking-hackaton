<template>
    <div class="code">
        <img :src=qr>
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
      
    }
  },
  props: {
      code: String,
      qr: String
  }
}
</script>

<style scoped>
.code {
  display: flex;
  flex-direction: column;
  align-items: center;
}
</style>
