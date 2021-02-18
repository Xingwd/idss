import instance from '@/api/base'

export function getIndexComponentHS300 (query) {
  return instance({
    url: '/stock/index_component/hs300',
    method: 'get',
    params: query
  })
}

export function postIndexComponentHS300 (data) {
  return instance({
    url: '/stock/index_component/hs300',
    method: 'post',
    data: data
  })
}
