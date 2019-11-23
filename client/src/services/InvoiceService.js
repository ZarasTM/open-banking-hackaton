import { httpClient } from './HttpClient';

export default {
  getUserData(nip) {
    return httpClient.post('/invoice/getUserData', nip);
  },
  createInvoice(invoiceId) {
    return httpClient.post('/invoice/createInvoice', invoiceId);
  },
  getInvoiceData(invoiceId) {
    return httpClient.post('/invoice/getInvoiceData', invoiceId);
  }
};
