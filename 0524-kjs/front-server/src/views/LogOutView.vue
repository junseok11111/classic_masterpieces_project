<template>
  <div id="logout">
    <p>{{'로그아웃중'}}</p>
    <img src="@/assets/logoutimg.jpg" alt="" id="logoutimg">
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