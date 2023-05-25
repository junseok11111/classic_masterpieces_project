<template>
  <div class="actor_card">
    <!-- <p>{{actor}}</p> -->
    <img :src="`http://image.tmdb.org/t/p/w92${actor?.profile_path}`" alt="...">
    <p>{{actor.name}}</p>
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
.actor_card {
  display: flex;
  flex-direction: column;
  width: 100px;
  margin-left: 20px;
  margin-right: 20px;
}
</style>