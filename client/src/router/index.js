import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Dashboard from "../views/Dashboard"
import Invoicing from "../views/Invoicing"
import Transactions from "../views/Transactions";
import store from "../store"

Vue.use(VueRouter);

const authGuard = (to, from, next) => {
  if (!store.state.isUserLoggedIn) {
    next('');
  } else {
    next();
  }
};


const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/dashboard',
    name: 'dashboard',
    beforeEnter: authGuard,
    component: Dashboard
  },
  {
    path: '/invoicing',
    name: 'invoicing',
    beforeEnter: authGuard,
    component: Invoicing
  },
  {
    path: '/transactions',
    name: 'transactions',
    beforeEnter: authGuard,
    component: Transactions
  }
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
});

export default router;
