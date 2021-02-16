import instance from '@/api/base'

export function getStocks (query) {
  return instance({
    url: '/stocks',
    method: 'get',
    params: query
  })
}

export function getStock (code, query) {
  return instance({
    url: '/stocks/{code}',
    method: 'get',
    params: query
  })
}

export function postStocks (query) {
  return instance({
    url: '/stocks/{code}',
    method: 'post',
    params: query
  })
}

export function postStock (code, query) {
  return instance({
    url: '/stocks/{code}',
    method: 'post',
    params: query
  })
}
