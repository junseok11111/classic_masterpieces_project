<template>
  <div>
    
      <tr class="articlelist">
        <td class="articlerouter">
          <router-link :to="{name: 'ArticleDetailView', params: {id: article.id}}" >
            {{article.title}}
          </router-link>
        </td>

        <td class="articleusername">{{article.user_name}}</td>
      </tr>
      <hr>
 
  </div>
</template>

<script>
export default {
  name: 'ArticleItem',
  props: {
    article: Object,
  }
}
</script>

<style>


.articlelist{
  max-width: 1000px;
  width: auto;



  padding: 20px;
 
  color: #ffffff;
}

.articlerouter{
  color: #ffffff;

  width: 700px;
 
}

.articleusername{
  color: #ffffff;

  width: 300px;

}
</style>