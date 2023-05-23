<template>
  <div class="SignUpView">
    <div class="containersign">
      <br />
      <br />
      <form @submit.prevent="signUp" class="formsign">
        <div class="form-group">
          <label for="username">Username:</label>
          <input
            type="text"
            id="username"
            v-model="username"
            class="form-control"
          />
        </div>

        <div class="form-group">
          <label for="password1">Password:</label>
          <input
            type="password"
            id="password1"
            v-model="password1"
            class="form-control"
          />
        </div>

        <div class="form-group">
          <label for="password2">Password Confirmation:</label>
          <input
            type="password"
            id="password2"
            v-model="password2"
            class="form-control"
          />
        </div>

        <button type="submit" class="btn btn-primary">Sign Up</button>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: "SignUpView",
  data() {
    return {
      username: null,
      password1: null,
      password2: null,
    };
  },
  methods: {
    signUp() {
      const username = this.username;
      const password1 = this.password1;
      const password2 = this.password2;

      const payload = {
        username,
        password1,
        password2,
      };

      this.$store.dispatch("signUp", payload);
    },
  },
};
</script>

<style>
.SignUpView {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-image: url("@/assets/86772212622_727.jpg");
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}


.SignUpView::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5); /* Adjust the opacity as needed */
}

  .containersign {
    max-width: 400px;
    width: 100%;
    background-color: rgba(247, 247, 247, 0.9);
    border: 1px solid #ddd;
    border-radius: 5px;
    padding: 20px;
    text-align: center; /* Center the form within the container */
  }
.formsign {
  padding: 20px;
  background-color: rgba(
    247,
    247,
    247,
    0.9
  ); /* Adjust the background color and opacity as needed */
  border: 1px solid #ddd;
  border-radius: 5px;
  position: relative;
  z-index: 2;
}

.form-group {
  margin-bottom: 15px;
}

label {
  display: inline-block;
  margin-bottom: 5px;
  font-weight: bold; /* Add a font-weight to make the labels more prominent */
  color: #333; /* Adjust the label color as needed */
}
.form-control {
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
  .containersign {
    max-width: 100%;
  }
}
</style>
