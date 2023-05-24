<template>
  <div class="LogInView">
    <div class="containerlogin">
      <br />
      <br />
      <form @submit.prevent="login" class="formlogin">
        <div class="form-logingroup">
          <label for="username">Username:</label>
          <input type="text" id="username" v-model="username" class="form-logincontrol">
        </div>

        <div class="form-logingroup">
          <label for="password">Password:</label>
          <input type="password" id="password" v-model="password" class="form-logincontrol">
        </div>

        <button type="submit" class="btn btn-primary">Log In</button>
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
        username,
        password
      }

      this.$store.dispatch('login', payload)
    }
  },
}
</script>

<style>
.LogInView {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-image: url("@/assets/86772212622_727.jpg");
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}

.containerlogin {
  max-width: 400px;
  width: 100%;
  background-color: rgba(247, 247, 247, 0.9);
  border: 1px solid #ddd;
  border-radius: 5px;
  padding: 20px;
  text-align: center; /* Center the form within the container */
}

  .LogInView::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
  }

.formlogin {
  padding: 20px;
  background-color: rgba(247, 247, 247, 0.9);
  border: 1px solid #ddd;
  border-radius: 5px;
  position: relative;
  z-index: 2;
}


.form-logingroup {
  margin-bottom: 15px;
}

label {
  display: inline-block;
  margin-bottom: 5px;
  font-weight: bold;
  color: #333;
}

.form-logincontrol {
  width: 90%;
  padding: 10px;
  font-size: 16px;
  border-radius: 3px;
  border: 1px solid #ddd;
}

.btn-primary {
  display: block;
  width: 100%;
  padding: 10px;
  font-size: 16px;
  text-align: center;
  background-color: #007bff;
  border: none;
  border-radius: 3px;
  color: #fff;
  cursor: pointer;
}

.btn-primary:hover {
  background-color: #0069d9;
}

@media screen and (max-width: 480px) {
  .formlogin {
    max-width: 100%;
  }
}
</style>
