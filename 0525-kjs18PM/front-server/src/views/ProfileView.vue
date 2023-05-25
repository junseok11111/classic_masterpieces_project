<template>
  <div class="profile">
    <div class="profileimg"></div>

    <div class="profile-info">
      <div class="profile-circle">
        <img class="profile-image" :src="user.avatar" alt="프로필 이미지" />
        <h3 class="profile-name">{{ user.name }}</h3>
      </div>
      <div class="profile-details">
        <h2>내가 쓴 댓글</h2>
        <h2>내가 쓴 게시글</h2>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ProfileView",
  data() {
    return {
      user: {
        name: "박지현",
        email: "qq@naver.com",
        age: 99,
        gender: "x",
        avatar: require("@/assets/박지현.jpg"),
      },
    };
  },
};
</script>

<style>
.profile {
  max-width: 1100px;
  margin: 0 auto;
  padding: 20px;
}

.profileimg {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 250px;
  background-image: url("@/assets/더넌귀신.jpg");
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}

.profile-circle {
  display: flex;
  align-items: center;
}

.profile-image {
  width: 200px;
  height: 200px;
  border-radius: 50%;
  object-fit: cover;
}

.profile-name {
  margin-left: 40px;
  font-size: 30px;
  color: white;
}

.profile-details {
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 20px;
}

@media (max-width: 768px) {
  .profile {
    margin: 0 20px;
  }

  .profileimg {
    height: 150px;
  }

  .profile-image {
    width: 150px;
    height: 150px;
  }

  .profile-name {
    margin-left: 20px;
    font-size: 20px;
  }

  .profile-details {
    margin-top: 10px;
  }
}
</style>
