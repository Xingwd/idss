import instance from '@/api/base'

export function getIndexComponentSH50 (query) {
  return instance({
    url: '/stock/index_component/sh50',
    method: 'get',
    params: query
  })
}

export function postIndexComponentSH50 (data) {
  return instance({
    url: '/stock/index_component/sh50',
    method: 'post',
    data: data
  })
}
