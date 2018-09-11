<doc>
Komponent używany do wyświetlenia pojedynczego posta
</doc>

<style lang="sass" rel="stylesheet/sass">
.post-element-container
  display: flex
  flex-direction: column
  width: 17em
  background-color: #F8F8FF
  padding: 0 1em 0 1em
  .post-title
    font-size: 1.5em
  .post-author
    color: grey
  .post-text
    font-size: 1.2em
  .post-date
    color: grey
    font-size: .8em
</style>

<template>
    <div class="post-element-container">
        <p class="post-title" @click="title_clicked">{{ post.title }}</p>
        <p class="post-author">Author: {{ post.author }}</p>
        <p class="post-text"><ellipsis :show-button="false" :ellipsis="'...'" :text="post.text" :line="5">
                    </ellipsis></p>
        <p class="post-date">{{ post.created_date | moment("DD.MM.YYYY") }}</p>
    </div>
</template>

<script type="text/babel">
import Ellipsis from 'ellipsis-plus';

export default {
    name: 'post-element',
    props: ['post'],
    components: {
        Ellipsis
    },
    data () {
        return {
        }
    },
    methods: {
        title_clicked () {
            this.$emit('title clicked', this.post.title);
        }
    }
}
</script>
