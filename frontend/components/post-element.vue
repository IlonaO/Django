<doc>
Komponent używany do wyświetlenia pojedynczego posta
</doc>

<style lang="sass" rel="stylesheet/sass">
.post-element-container
  background-color: red
</style>

<template>
    <div class="post-element-container">
        <p>post</p>
        {{ post }}
    </div>
</template>

<script type="text/babel">

export default {
    name: 'post-element',
    props: ['post'],
    data () {
        return {
        }
    },
}
</script>
