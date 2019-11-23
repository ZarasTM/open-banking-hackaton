import { httpClient } from './HttpClient';

export default {
  getUserData(tin) {
    return httpClient.post('/invoice/getUserData', tin);
  },
  createInvoice(invoiceId) {
    return httpClient.post('/invoice/createInvoice', invoiceId);
  },
  getInvoiceData(invoiceId) {
    return httpClient.post('/invoice/getInvoiceData', invoiceId);
  },
  getInvoicesSummary() {
    return httpClient.post('/invoice/getInvoicesSummary')
  }
};
