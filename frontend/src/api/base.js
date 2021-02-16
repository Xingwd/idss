import axios from 'axios'
// import { showLoading, hideLoading } from '@/utils/loading'

// Create an instance
const instance = axios.create({
  baseURL: process.env.VUE_APP_BASE_URL,
  timeout: 15000
})

// Add a request interceptor
instance.interceptors.request.use(
  config => {
    // showLoading()
    return config
  },
  error => {
    // showLoading()
    return Promise.reject(error)
  }
)

// Add a response interceptor
instance.interceptors.response.use(
  response => {
    // hideLoading()
    return response
  },
  error => {
    // hideLoading()
    return Promise.reject(error.response)
  }
)

export default instance
