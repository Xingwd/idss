<template>
  <v-app>
    <v-navigation-drawer
      v-model="drawer"
      app
      clipped
      expand-on-hover
      floating
      style="max-width: 200px"
    >
      <v-list dense>
        <v-list-item
          link
          to="/"
        >
          <v-list-item-action>
            <v-icon>mdi-home</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>自选</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item
          link
          to="/xuangu"
        >
          <v-list-item-action>
            <v-icon>mdi-feather</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>选股</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    <v-app-bar
      app
      clipped-left
      color="white"
    >
      <v-app-bar-nav-icon @click.stop="drawer = !drawer" />
      <v-toolbar-title>SEER</v-toolbar-title>
    </v-app-bar>
    <v-main>
      <router-view />
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
    drawer: true
  })
}
</script>
