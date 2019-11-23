import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex);

export default new Vuex.Store({
  strict: true,
  state: {
    isUserLoggedIn: false,
  },
  mutations: {
    logIn(state){
      state.isUserLoggedIn = true
    },
    logOut(state){
      state.isUserLoggedIn = false
    },
  },
  actions: {
    logIn({commit}){
      commit('logIn');
    },
    logOut({commit}){
      commit('logOut');
    }
  }
})
