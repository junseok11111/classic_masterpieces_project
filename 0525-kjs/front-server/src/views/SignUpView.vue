<template>
  <div class="AccountsView">
    <div class="centered-div" @click.stop>

      <form @submit.prevent="signUp" class="form-container">
        <h2 class="guide-text">회원가입</h2> 

        <input type="text" id="username" v-model="username" placeholder="아이디를 입력하세요"><br>
        <input type="password" id="password1" v-model="password1" placeholder="비밀번호를 입력하세요"><br>
        <input type="password" id="password2" v-model="password2" placeholder="비밀번호를 확인하세요">

        <input type="submit" value="SignUp" class="submit-button">
      </form>

    </div>
  </div>
</template>

<script>
export default {
  name: 'SignUpView',
  data() {
    return {
      username: null,
      password1: null,
      password2: null,
    }
  },
  methods: {
    signUp() {
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2

      const payload = {
        username, password1, password2
      }
      this.$store.dispatch('signUp', payload)

    }
  }
}
</script>

<style>
</style>