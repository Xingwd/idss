<template>
  <v-container fluid>
    <v-row>
      <v-col>
        <v-data-table
          class="elevation-1"
          :headers="headers"
          fixed-header
          :items="datasets"
          :page.sync="page"
          :items-per-page.sync="pageSize"
          :server-items-length.sync="itemsLength"
          :footer-props="footerProps"
          :height="height"
          :loading="loading"
          @pagination="handlePagination"
        >
          <template v-slot:top>
            <v-toolbar
              flat
            >
              <v-toolbar-title>上证50成分股</v-toolbar-title>
              <v-divider
                class="mx-4"
                inset
                vertical
              ></v-divider>
              <v-spacer></v-spacer>
              <template>
                <v-btn
                  color="primary"
                  class="mb-2"
                  @click="handleSync"
                >
                  同步
                </v-btn>
              </template>
            </v-toolbar>
          </template>
          <template v-slot:item.stock_overview="{ item }">
            <a
              small
              class="mr-2"
              @click="linkToStockData(item)"
            >
              数据
            </a>
            <a
              small
              @click="linkToZJLX(item)"
            >
              资金流向
            </a>
          </template>
        </v-data-table>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { getIndexComponentSH50, postIndexComponentSH50 } from '@/api/stock/index_component/sh50'

export default {
  data () {
    return {
      headers: [
        { text: 'ID', align: 'start', sortable: false, value: 'id' },
        { text: '股票代码', align: 'start', sortable: false, value: 'code' },
        { text: '股票名称', sortable: false, value: 'name' },
        { text: '同步时间', sortable: false, value: 'sync_time' },
        { text: '个股概况(东方财富网)', value: 'stock_overview', sortable: false }
      ],
      datasets: [],
      footerProps: {
        itemsPerPageOptions: [15, 30, 45, -1],
        showCurrentPage: true,
        showFirstLastPage: true
      },
      page: 1,
      pageSize: 15,
      itemsLength: 300,
      loading: false
    }
  },
  mounted () {
    this.setDataSets()
  },
  computed: {
    height: function () {
      return document.documentElement.clientHeight - 259
    }
  },
  methods: {
    setDataSets () {
      this.loading = true
      const query = {
        page: this.page,
        page_size: this.pageSize
      }
      getIndexComponentSH50(query
      ).then(response => {
        this.datasets = response.data.items
        this.itemsLength = response.data.total
      }).catch(error => {
        console.log(error)
      })
      this.loading = false
    },
    handlePagination (pagination) {
      this.setDataSets()
    },
    handleSync () {
      postIndexComponentSH50({}
      ).then(response => {
        this.page = 1
        this.setDataSets()
      }).catch(error => {
        console.log(error)
      })
    },
    linkToStockData (item) {
      const url = 'http://data.eastmoney.com/stockdata/{}.html'.replace('{}', item.code)
      window.open(url)
    },
    linkToZJLX (item) {
      const url = 'http://data.eastmoney.com/zjlx/{}.html'.replace('{}', item.code)
      window.open(url)
    }
  }
}
</script>
