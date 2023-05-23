<template>
  <div class="AccountsView" @click="moveDoorView">

    <div class="centered-div" @click.stop>
      <h2 class="guide-text">로그인</h2>
      <form @submit.prevent="login" class="form-container">
        <input type="text" id="username" v-model="username" placeholder="아이디를 입력하세요"><br>
        <input type="password" id="password" v-model="password" placeholder="비밀번호를 입력하세요"><br>

        <input type="submit" value="logIn" class="submit-button">
      </form>

    </div>
  </div>
</template>

<script>
export default {
  name: 'LogInView',
  data() {
    return {
      username: null,
      password: null,
    }
  },
  methods: {
    login() {
      const username = this.username
      const password = this.password

      const payload = {
        username, password
      }
      this.$store.dispatch('login', payload)
    },
    moveDoorView() {
      this.$router.push({name: 'DoorView'})
    }
  }
}
</script>

<style>
.AccountsView {
  height: 100vh;
  background-image: url("@/assets/86772212622_727.jpg");
  background-color: rgba(0, 0, 0, 0.9);
  background-size: cover;
  position: relative;
}

.AccountsView::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
}

.centered-div {
  position: relative;
  width: 350px;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -70%);
  z-index: 2;
  text-align: left;
}

.guide-text {
  text-align: left;
  color: white;
  font: bold;
  margin: 15px;
}

.form-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  /* background-color: rgba(0, 0, 0, 0.3); */
  /* border-radius: 5px; */
}

.form-container > input {
  width: 300px;
  padding: 10px;
  font-size: 20px;
  border-radius: 3px;
  border: 1px solid #ddd;
}

.submit-button {
  display: block;
  width: 70%;
  margin-top: 5%;

  padding: 10px;
  font-size: 16px;
  background-color: #007bff;
  border: none;
  border-radius: 3px;
  color: #fff;
  cursor: pointer;
}

.submit-button:hover {
  background-color: #0069d9;
}

</style>