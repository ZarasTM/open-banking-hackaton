import { httpClient } from './HttpClient';

export default {
  register(userData) {
    return httpClient.post('/auth/register', userData);
  },
  login(userData) {
    return httpClient.post('/auth/login', userData);
  },
  isLogged() {
    return httpClient.post('/auth/isLogged');
  },
  logout(){
    return httpClient.post('/auth/logout');
  },
  tokenValid(){
    return httpClient.post('/tokenValid');
  },
  generateToken(){
    return httpClient.post('/generateToken');
  }
};
