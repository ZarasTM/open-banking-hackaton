import axios from 'axios';

let apiBaseUrl = 'http://192.168.1.24:5000';

const config = {
  baseURL: apiBaseUrl,
  withCredentials: true,
  timeout: 3000
};

const httpClient = axios.create(config);

export { httpClient };
