<doc>
Komponent używany do wyświetlenia postów
</doc>

<style lang="sass" rel="stylesheet/sass">
/*@import "../base.sass"*/
.posts-container
  background-color: red
</style>

<template>
    <div class="posts-container">
        <div>Posts will be here</div>
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
        }
    },
    computed: {
    },
    methods: {
    },
    mounted () {
    }

}
</script>
