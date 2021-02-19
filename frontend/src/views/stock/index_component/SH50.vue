<template>
  <v-container fluid>
    <v-row>
      <v-col>
        <v-btn
          block
          color="primary"
          @click="handleSync"
        >
          同步
        </v-btn>
      </v-col>
    </v-row>
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
        ></v-data-table>
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
        { text: '同步时间', sortable: false, value: 'sync_time' }
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
      return document.documentElement.clientHeight - 255
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
    }
  }
}
</script>
