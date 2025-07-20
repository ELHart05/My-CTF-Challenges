<template>
    <section class="main">
        <BlogPostView v-if="!userState" :post="welcomeScreen" />
        <BlogPostView :post="post" v-for="(post, index) in mainBlogPosts" :key="index" />
    </section>
</template>

<script>
    import {
        mapGetters,
        mapState
    } from 'vuex';
    import BlogPostView from './BlogPostView.vue';
    export default {
        name: 'MainSectionView',
        components: {
            BlogPostView
        },
        data() {
            return {
                welcomeScreen: {
                    title: 'WELCOME!',
                    blogPost: "Welcome to the Sh3llBl0g5 managed by ELGladiator, enjoy the content!, don't try to look for vulnerabilities, I'm watching you!, know your role and you know the rest...",
                    photo: 'https://linktr.ee/og/image/shellmates.jpg',
                    welcomeScreen: true
                }
            }
        },
        computed: {
            ...mapGetters(['mainBlogPosts']),
            ...mapState(['userState'])
        }
    }
</script>

<style lang="scss" scoped>
    @use '../../assets/sass/mixins.scss'as *;

    .main {
        display: flex;
        flex-direction: column;
    }
</style>