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
    path: '/stock/index_component',
    redirect: { name: 'hs300' },
    component: () => import(/* webpackChunkName: "stock_index_component" */ '../views/stock/index_component/IndexComponent.vue'),
    children: [
      {
        path: 'sh50',
        name: 'SH50',
        component: () => import(/* webpackChunkName: "stock_index_component" */ '../views/stock/index_component/SH50.vue')
      },
      {
        path: 'hs300',
        name: 'HS300',
        component: () => import(/* webpackChunkName: "stock_index_component" */ '../views/stock/index_component/HS300.vue')
      }
    ]
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  }
]

const router = new VueRouter({
  routes
})

export default router
