<template>
  <div class="video-background">

    <!-- 1) 비디오  -->
    <video ref="myVideo" class="video-element" autoplay muted loop>
      <source :src="videoPath" type="video/mp4">
    </video>

    <!--2) 문구 -->
    <div class="overlay-text" :style="{ fontSize: calculatedFontSize }">
      한 순간도 방심하지 마세요
    </div>

  </div>
</template>

<script>
export default {
  name: 'DoorView',

  data() {
    return {
      // 1) 비디오 경로
      videoPath: require('@/assets/door_sample_video.mp4'),

      // 2) 글자 사이즈
      calculatedFontSize: '3rem'
    }
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

  methods:{

    // 2)폰트
    updateFontSize() {
      // 화면 너비에 따라 폰트 크기 계산 
      const screenWidth = window.innerWidth;
      const calculatedSize = screenWidth / 40; // 임의로 폰트 크기 계산식 설정
      
      this.calculatedFontSize = `${calculatedSize}px`;
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
</style>