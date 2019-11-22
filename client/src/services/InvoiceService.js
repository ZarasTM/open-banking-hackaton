import { httpClient } from './HttpClient';

export default {
  getUserData(nip) {
    return httpClient.post('/invoice/getUserData', nip);
  }
};
