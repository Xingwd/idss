import instance from '@/api/base'

export function getHS300Stocks (query) {
  return instance({
    url: '/xuangu/hs300',
    method: 'get',
    params: query
  })
}

export function postHS300Stocks (data) {
  return instance({
    url: '/xuangu/hs300',
    method: 'post',
    data: data
  })
}
