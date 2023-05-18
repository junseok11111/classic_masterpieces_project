<template>
  <div>
    <!-- <p>{{actor}}</p> -->
    <img :src="`http://image.tmdb.org/t/p/w92${actor?.profile_path}`" alt="...">
    <p>이름: {{actor.name}}</p>

  </div>
</template>

<script>
export default {
  name: 'ActorCard',
  props: {
    actor: Object,
  },
}
</script>

<style>

</style>