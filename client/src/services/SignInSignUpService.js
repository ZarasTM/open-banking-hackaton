import { httpClient } from './HttpClient';

export default {
  register(userData) {
    return httpClient.post('/auth/register', userData);
  }
};
