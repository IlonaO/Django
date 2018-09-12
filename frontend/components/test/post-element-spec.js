import Vue from 'vue'
import VueI18n from 'vue-i18n'
import PostElement from '../post-element.vue'
import { mount } from '@vue/test-utils'


Vue.use(VueI18n);
Vue.use(require('vue-moment'));

describe("post-element", () => {
    function get_comp_instance(Component, propsData) {
        const Ctor = Vue.extend(Component);
        const vm = new Ctor({propsData}).$mount();
        return vm
    }

    const PE = get_comp_instance(PostElement,
        {
            post: {
                id: 1,
                created_date: "2018-08-10",
                author: "someuser",
                text: "Some post content",
                title: "Title"
            }
        });

    // with vue test utils

    const PE_wrapper = mount(PostElement, {
        propsData: {
            post: {
                id: 1,
                created_date: "2018-08-10",
                author: "someuser",
                text: "Some post content",
                title: "Title"
            }
        }
    });

    beforeEach(function () {
        spyOn(PE, "$emit");
        spyOn(PE_wrapper.vm, "$emit");
    });

    it("Rendering check and emit with test-utils", () => {
        let post_title = PE_wrapper.find('.post-title');
        expect(post_title.exists()).toBeTruthy();
        post_title.trigger('click');
        expect(PE_wrapper.vm.$emit).toHaveBeenCalledWith('title clicked', 'Title');
    });

    it("Rendering check", () => {
        expect(PE.$el.querySelector('.post-title').textContent).toBe('Title');
        expect(PE.$el.querySelector('.post-author').textContent).toBe('Author: someuser');
        expect(PE.$el.querySelector('.post-text').textContent).toBe('Some post content ');
        expect(PE.$el.querySelector('.post-date').textContent).toBe('10.08.2018');
    });

    it("Check emitting after clicking title", () => {
        PE.$el.querySelector('.post-title').click();
        expect(PE.$emit).toHaveBeenCalledWith('title clicked', 'Title');
    });

});
