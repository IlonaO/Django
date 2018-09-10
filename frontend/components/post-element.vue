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
        <post-element></post-element>
    </div>
</template>

<script type="text/babel">

export default {
    name: 'post-element',
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
