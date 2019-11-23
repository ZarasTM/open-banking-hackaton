import { httpClient } from './HttpClient';

export default {
  fetchUserData() {
    return httpClient.post('/user/fetchUserData');
  }
};
