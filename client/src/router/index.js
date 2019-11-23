import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Dashboard from "../views/Dashboard"
import Invoicing from "../views/Invoicing"
import Transactions from "../views/Transactions";

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/dashboard',
    name: 'dashboard',
    component: Dashboard
  },
  {
    path: '/invoicing',
    name: 'invoicing',
    component: Invoicing
  },
  {
    path: '/transactions',
    name: 'transactions',
    component: Transactions
  }
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
});

export default router;
