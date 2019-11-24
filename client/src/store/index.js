import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex);

export default new Vuex.Store({
  strict: true,
  state: {
    isUserLoggedIn: false,
    user: {}
  },
  mutations: {
    logIn(state){
      state.isUserLoggedIn = true
    },
    logOut(state){
      state.isUserLoggedIn = false
    },
    setUser(state, user){
      state.user = user 
    }
  },
  actions: {
    logIn({commit}){
      commit('logIn');
    },
    logOut({commit}){
      commit('logOut');
    },
    setUser({commit}, user){
      commit('setUser', user)
    }
  }
})
