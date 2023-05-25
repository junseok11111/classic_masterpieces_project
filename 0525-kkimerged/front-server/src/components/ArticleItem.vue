<template>
  <div>
    <tr class="articlelist">
      <td class="articlerouter">
        <router-link
          :to="{ name: 'ArticleDetailView', params: { id: article.id } }"
        >
          {{ article.title }}
        </router-link>
      </td>

      <td class="articleusername">{{ article.user_name }}</td>
      <!-- <td class="articletime">{{ formattedTime }}</td> -->
    </tr>
  </div>
</template>

<script>
// import moment from "moment";

export default {
  name: "ArticleItem",
  props: {
    article: Object,
  },
  computed: {
    // formattedTime() {
    //   return moment(this.article.created_at).format("HH:mm");
    // },
  },
};
</script>

<style>
.articlelist {
  max-width: 1300px;
  width: auto;
  padding: 20px;
  color: #ffffff;
 
  
}
.articlerouter {
  color: rgb(165, 163, 163); /* Set the color of the router link to gray */
  border-bottom: solid;
  width: 700px;
  text-align: center;
}

.articlerouter a {
  display: inline-block;
  text-decoration: none;
  color: inherit;
  width: 100%; /* Make the router link occupy the full width of its container */
}

.articlerouter a:hover {
  text-decoration: underline; /* Add underline on hover if desired */
}

.articlerouter .router-link-exact-active {
  font-weight: bold; /* Optional: Add a visual indicator for the active router link */
}



.articleusername {
  color: rgb(165, 163, 163);
  border-bottom: solid;
  width: 300px;
  height: 30px;
}

.articletime {
  color: rgb(165, 163, 163);
  border-bottom: solid;
  width: 300px;
  height: 30px;
}
</style>
