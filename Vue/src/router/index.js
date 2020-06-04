import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/layout',
    name: 'Layout',
    component: () => import('../components/Layout.vue')
  },
  {
    path: '/label',
    name: 'Label',
    component: () => import('../components/Label.vue')
  },
  {
    path: '/popup',
    name: 'Popup',
    component: () => import('../components/Popup.vue')
  },
  {
    path: '/tree',
    name: 'Tree',
    component: () => import('../components/Tree.vue')
  },
  {
    path: '/pump',
    name: 'Pump',
    component: () => import('../components/Pump.vue')
  },
  {
    path: '/water',
    name: 'Water',
    component: () => import('../components/Water')
  },
  {
    path: '/rest',
    name: 'Rest',
    component: () => import('../components/Rest')
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
