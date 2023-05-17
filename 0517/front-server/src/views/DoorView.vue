<template>

  <div class="video-background">
     <nav class="navbar">
      <router-link :to="{name: 'home'}">Home</router-link> |
    </nav>
    <video ref="myVideo" class="video-element" autoplay muted loop>
       <source :src="videoPath" type="video/mp4">
    </video>
    <div class="overlay-text">영화, 드라마, 예능, 다큐멘터리, 웹툰을 무제한으로 매주 5백 여편의 신작이 업데이트 되며, 추가 요금은 전혀 없어요.</div>
    <div class="button-container">
        <button class="pink-button"></button>
    </div>
  
  </div>
  
</template>

<script>
export default {
  name: 'DoorView',
  data() {
    return {
      videoPath: require('@/assets/LifeIsBeautiful.mp4')
    };
  },
  mounted() {
    this.$refs.myVideo.play().catch(error => {
      console.error('Failed to play video:', error);
    });
  }
  // 컴포넌트 옵션
}
</script>

<style>
.navbar {
  position: absolute;
  top: 10px;
  left: 10px;
  z-index: 1;
  background-color: black;
  width: 100%;
  display: flex; /* Ensures flexbox layout */
  justify-content: flex-end; /* Aligns items to the left */
  align-items: center; /* Vertically aligns items */
}

.navbar router-link {
  margin-right: 0px; /* Adds some spacing between links */
}
.video-background {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  overflow: hidden;
  z-index: -1;
}

.video-element {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  min-width: 100%;
  min-height: 100%;
  width: auto;
  height: auto;
}

.overlay-text {
  position: absolute;
  top: 40%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-size: 50px;
  font-weight: bold;
  color: white;
  text-align: center;
}

.pink-button {
  position: absolute;
  top: 60%;
  width: 100px;
  height: 50px;
  background-color: pink;
  border-radius: 50%;
  border: none;
}

</style>

