<template>
  <v-app>
    <v-navigation-drawer
      v-model="drawer"
      app
      clipped
      floating
    >
      <v-list dense>
        <v-list-item
          link
          to="/"
        >
          <v-list-item-icon>
            <v-icon>mdi-home</v-icon>
          </v-list-item-icon>
          <v-list-item-title>主页</v-list-item-title>
        </v-list-item>
        <v-list-group
          :value="true"
          prepend-icon="mdi-clipboard-text-multiple"
          no-action
        >
          <template v-slot:activator>
            <v-list-item-title>指数成分</v-list-item-title>
          </template>

          <v-list-item
            v-for="([title, icon, to], i) in stock_indexs"
            :key="i"
            link
            :to="to"
          >
            <v-list-item-title v-text="title"></v-list-item-title>
            <v-list-item-icon>
              <v-icon v-text="icon"></v-icon>
            </v-list-item-icon>
          </v-list-item>
        </v-list-group>
      </v-list>
    </v-navigation-drawer>
    <v-app-bar
      app
      clipped-left
    >
      <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
      <!-- <v-toolbar-title>SEER</v-toolbar-title> -->
    </v-app-bar>
    <v-main>
      <router-view></router-view>
    </v-main>
    <v-footer
      app
      padless
      class="font-weight-medium"
    >
      <v-col
        class="text-center"
        cols="12"
      >
        &copy; {{ new Date().getFullYear() }} — <strong>邢为栋</strong>
      </v-col>
    </v-footer>
  </v-app>
</template>

<script>
export default {
  data: () => ({
    drawer: true,
    stock_indexs: [
      ['上证50成分', 'mdi-clipboard-text', '/stock/index_component/sh50'],
      ['沪深300成分', 'mdi-clipboard-text', '/stock/index_component/hs300']
    ]
  })
}
</script>
