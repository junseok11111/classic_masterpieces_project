<template>

  <div class="video-background">
     <nav class="navbar">
      <router-link :to="{name: 'home'}">Home</router-link> |
    </nav>

    <!-- 1) 비디오  -->
    <video ref="myVideo" class="video-element" autoplay muted loop>
       <source :src="videoPath" type="video/mp4">
    </video>

    <!--2) 문구 -->
    <div class="overlay-text" :style="{ fontSize: calculatedFontSize }">
      고전 명작의 즐거움을 느껴 보세요
    </div>

    <!-- 버튼 -->    
    <div class="button-container" :style="{ fontSize: calculatedFontSize }">
        <button class="button"></button>
    </div>
  
  </div>
  
</template>

<script>
export default {
  name: 'DoorView',


  data() {

    return {
      // 1) 비디오 경로
      videoPath: require('@/assets/LifeIsBeautiful.mp4'),

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
      const calculatedSize = screenWidth / 20; // 임의로 폰트 크기 계산식 설정
      
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
  justify-content: flex-end;
  align-items: center;
  padding: 0 10px;
}

.navbar router-link {
  margin-left: 0;
  margin-right: 10px;
  color: white; /* Added: Sets the link color to white */
  text-decoration: none; /* Added: Removes the default link underline */
}
.navbar router-link:first-child {
  margin-left: auto; /* 변경: 첫 번째 링크를 오른쪽으로 이동 */
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

