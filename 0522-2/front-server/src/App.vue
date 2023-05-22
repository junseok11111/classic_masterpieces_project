<template>
  <div id="app">
    <nav class="navbar">
      <div class="navbar-header">
        <div class="navbar-left">
          <img src="@/assets/sample_site_logo.png" alt="로고" class="logo">
        </div>
        <div class="navbar-right">
          <router-link :to="{name: 'home'}" class="navbar-link">Home</router-link> |
          <router-link :to="{name: 'UpComingView'}" class="navbar-link">Upcoming</router-link> |
          <router-link :to="{name: 'SignUpView'}" class="navbar-link">SignUp</router-link> |
          <router-link :to="{name: 'LogInView'}" class="navbar-link">LogIn</router-link> |
        </div>
      </div>
    </nav>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'AppView',
  methods: {
    // Top Rated 영화 정보 요청
    getTopRatedMovies() {
      this.$store.dispatch('getTopRatedMovies')
    },
  },
  created() {
    this.getTopRatedMovies()
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  background-color: black;
}

nav {
  padding: 30px;
  margin: 0;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}

.navbar {
  position: absolute;
  top: 0px;
  right: 0px;
  left: 0;
  height: 60px;
  z-index: 1;
  background-color: black;
  margin: 0px;
  display: flex;
  justify-content: space-between;  
  align-items: center; 
  padding: 0 10px; 
}

.navbar-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
}
.navbar-left {
  margin-left: auto;
  display: flex;
  align-items: center;
  flex: 1; 
}

.navbar-right {
  display: flex;
  align-items: center;
    flex: 1; /* 수정된 부분 */
  justify-content: flex-end; /* 수정된 부분 */
}

.navbar-link {
  margin-left: 10px;
  color: white;
  text-decoration: none;
}

.logo {
  width: 80px; /* 로고 이미지의 크기를 조정합니다. */
  height: auto;
  margin-right: auto;
}
</style>