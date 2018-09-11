import Vue from 'vue';

Vue.config.lang = 'pl';
Vue.config.devtools = true;

import Posts from './components/posts.vue';
import PostElement from './components/post-element.vue';

new Vue({
    el: '#vue-app',
    components: {
        Posts,
        PostElement
    },
    data () {
        return {}
    }
});
