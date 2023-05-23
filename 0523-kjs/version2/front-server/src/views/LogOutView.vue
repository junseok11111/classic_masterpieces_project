<template>
  <div>
    <p>{{'로그아웃중'}}</p>
  </div>
</template>

<script>
export default {
  name: 'LogOutView',
  methods: {
    logout() {
      this.$router.push({name : 'DoorView'})
    }
  },
  created() {
    this.logout()
  }
}
</script>

<style>

</style>