import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import Login from './views/Login.vue'

Vue.use(Router);

const routes = [
    {
        path: '/',
        component: Home,
        meta: {requiresAuth: true}
    },
    {
        path: '/login',
        component: Login,
    },

];

const router = new Router({
    routes: routes,
});

router.beforeEach((to, from, next) => {
    let token = localStorage.getItem('token');
    let requireAuth = to.matched.some(record => record.meta.requiresAuth);

    if (!requireAuth) {
        next();
    }

    if (requireAuth && !token) {
        next('/login');
    }

    if (to.path === '/login') {
        next()
    }

    if (requireAuth && token) {
        next();
    }
});

export default router;