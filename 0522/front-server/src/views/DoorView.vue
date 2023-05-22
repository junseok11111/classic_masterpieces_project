<template>

  <div class="video-background">


     <nav class="navbar">
 
        <div class="navbar-header">
          <div class="navbar-left">
            <img src="../assets/7a57b8e8-4029-4220-8d9f-2b1c89b2c1e5.png" alt="로고" class="logo">
          </div>
          <div class="navbar-right">
            <router-link :to="{name: 'home'}" class="navbar-link">Home</router-link>
          </div>
        
      </div>
    </nav>

    <!-- 1) 비디오  -->
    <video ref="myVideo" class="video-element" autoplay muted loop>
       <source :src="videoPath" type="video/mp4">
    </video>

    <!--2) 문구 -->
    <div class="overlay-text" :style="{ fontSize: calculatedFontSize }">
      숨막히는 공포를 느껴 보세요
    </div>

    <!-- 버튼 -->    
    <div class="button-container" :style="{ fontSize: calculatedFontSize }">
        <button class="button"></button>
    </div>
  <template>
 
</template>
  </div>
  
</template>

<script>
export default {
  name: 'DoorView',


  data() {

    return {
      // 1) 비디오 경로
      videoPath: require('@/assets/THE NUN - Official Teaser Trailer [HD] (2) (online-video-cutter.com) (1).mp4'),

      // 2) 글자 사이즈
      calculatedFontSize: '3rem'
  
    };
  },


  mounted() {
    // 1)비디오 
    this.$refs.myVideo.play()
    .catch(error => {
      console.error('Failed to play video:', error);
      
    });
    // 2)폰트
      window.addEventListener('resize', this.updateFontSize);
      window.removeEventListener('resize', this.updateButtonPosition);
    },
    beforeDestroy() {
      window.removeEventListener('resize', this.updateFontSize);
      window.removeEventListener('resize', this.updateButtonPosition);
    },


    // 3)버튼
    

  methods:{

    // 2)폰트
    updateFontSize() {
      // 화면 너비에 따라 폰트 크기 계산 
      const screenWidth = window.innerWidth;
      const calculatedSize = screenWidth / 40; // 임의로 폰트 크기 계산식 설정
      
      this.calculatedFontSize = `${calculatedSize}px`;
    },

    // 3)버튼
      updateButtonPosition() {
    // Calculate the button's top and left positions based on screen size
    const screenHeight = window.innerHeight;
    const screenWidth = window.innerWidth;
    const calculatedButtonTop = screenHeight * 0.6; // Adjust the percentage as needed
    const calculatedButtonLeft = screenWidth * 0.5; // Adjust the percentage as needed
    
    this.calculatedButtonTop = `${calculatedButtonTop}px`;
    this.calculatedButtonLeft = `${calculatedButtonLeft}px`;
  },

  


  }
  
  // 컴포넌트 옵션
}
</script>

<style>
body {
  margin: 0;
  padding: 0;
  overflow: hidden;
}

/* 네비게이션 */

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
/* 비디오 */
.video-background {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  overflow: hidden;
  z-index: -1;
  margin-left : 0px;

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


/* 문구 */
.overlay-text {
  position: absolute;
  top: 40%;
  left: 50%;
  transform: translate(-50%, -50%);
  /* font-size: 50px; */
  font-weight: bold;
  color: white;
  text-align: center;
  white-space: nowrap; 

}


.button {
  position: fixed;
  top: 60%;
  width: 100px;
  height: 50px;
  background-color: red;
  border-radius: 50%;
  border: none;
}

</style>

