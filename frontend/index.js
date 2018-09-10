import Vue from 'vue';
import VueI18n from 'vue-i18n';

Vue.use(VueI18n);
Vue.use(Vuex);

Vue.config.lang = 'pl';
Vue.locale('pl', {});
Vue.config.devtools = true;

import Posts from './components/posts.vue';
import PostElement from './components/post-element.vue'

// Run app
new Vue({
    el: '#vue-app',
    components: {
        Posts,
        PostElement
    },
    data () {
        return {}
    },
    created () {
    },
    mounted () {},
    computed: {},
    methods: {}
});
