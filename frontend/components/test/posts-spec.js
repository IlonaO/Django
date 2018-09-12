import Vue from 'vue'
import VueI18n from 'vue-i18n'
import Posts from '../posts.vue'

Vue.use(VueI18n);
Vue.use(require('vue-moment'));

describe("posts", () => {
    function get_comp_instance(Component, propsData) {
        const Ctor = Vue.extend(Component);
        const vm = new Ctor({propsData});
        vm.axios = {
            post: function () {
                return {then: function () {
                    vm.$emit('database_changed', vm.dataset);
                    vm.archived_dataset = true;
                }}
            }
        };
        return vm.$mount()
    }

    const P = get_comp_instance(Posts, {});

    P.posts = [{post: {id: 1, created_date: "2018-08-10", author: "someuser",
                    text: "Some post content", title: "Title"}},
                {post: {id: 2, created_date: "2018-08-10", author: "someuser2",
                    text: "Another post content", title: "Title2"}}];


    it("Checking methods", () => {
        expect(typeof P.fetch).toBe('function');
    });


    it("Checking data", () => {
        expect(P.posts).toEqual([
            {post: {id: 1, created_date: "2018-08-10", author: "someuser", text: "Some post content", title: "Title"}},
            {post: {id: 2, created_date: "2018-08-10", author: "someuser2", text: "Another post content", title: "Title2"}}
        ]);
    });

    it("Check rendering", () => {
        expect(P.$el.querySelector('.title').textContent).toBe('Posts');
    });

});
