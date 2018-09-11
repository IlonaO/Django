<doc>
Komponent używany do wyświetlenia postów
</doc>

<style lang="sass" rel="stylesheet/sass">
.posts-container
  font-family: Arial
  .posts-title
    display: flex
    justify-content: center
    .title
      font-size: 2em
  .posts
    display: flex
    justify-content: space-around
    .post-container-element
      display: flex
      flex: 0 1 auto
      width: 17em
  .add-new
    display: flex
    justify-content: center
    margin-top: 4em
</style>

<template>
    <div class="posts-container">
        <div class="posts-title">
            <p class="title">Posts</p>
        </div>
        <div class="posts">
            <div class="post-container-element" v-for="post in posts" v-bind:key="post.id">
                <post-element :post="post" v-on:title_clicked=""></post-element>
            </div>
        </div>
        <div class="add-new">
            <button @click="add_new">+</button>
        </div>
    </div>
</template>

<script type="text/babel">
import PostElement from "./post-element.vue";

export default {
    name: 'posts',
    components: {
        PostElement
    },
    props: [],
    data () {
        return {
            posts: null,
        }
    },
    created() {
        this.fetch();
    },
    methods: {
        fetch () {
            this.axios.get('get_posts/', {baseURL: '/xhr/', params: {}})
                .then((response) => {
                this.posts = response.data.objects;
            })
        },
        add_new () {

        }
    }

}
</script>
