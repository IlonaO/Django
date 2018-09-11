import Vue from 'vue';
import axios from 'axios';
import VueAxios from 'vue-axios';

Vue.config.lang = 'pl';
Vue.config.devtools = true;
Vue.use(require('vue-moment'));
Vue.use(VueAxios, axios);

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
