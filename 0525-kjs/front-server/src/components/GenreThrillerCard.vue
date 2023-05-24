<template>
  <div>
    <h1>뽑히나?</h1>
    <p>{{movie.title}}</p>
  </div>
</template>

<script>
export default {
  name: 'GenreThrillerCard',
  props: {
    movie: Object,
  }
}
</script>

<style>

</style>