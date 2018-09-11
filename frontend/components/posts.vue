<doc>
Komponent używany do wyświetlenia postów
</doc>

<style lang="sass" rel="stylesheet/sass">
.posts-container
  background-color: red
</style>

<template>
    <div class="posts-container">
        <div>Posts</div>
        <post-element></post-element>
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
                console.log(response);
            })
        }
    }

}
</script>
