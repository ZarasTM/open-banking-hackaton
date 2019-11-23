import { httpClient } from './HttpClient';

export default {
  getTransactionsSummary() {
    return httpClient.post('/transaction/getTransactionsSummary')
  }
};
