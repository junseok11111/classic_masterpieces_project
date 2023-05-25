<template>
  <div id="logout">
    <img src="@/assets/logoutimg2.jpg" alt="" id="logoutimg">
  </div>
</template>

<script>
export default {
  name: 'LogOutView',
  methods: {
    // logout() {
    //   this.$router.push({name : 'DoorView'})
    // }
  },
  created() {
    setTimeout(() => {
      this.$router.push({name : 'DoorView'})
    }, 600)
  }
}
</script>

<style>
#logout {
  background-color: black;
  height: 1000px;
}

#logoutimg {
  width: 1000px;
}
</style>