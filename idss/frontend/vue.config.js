module.exports = {
  transpileDependencies: [
    'vuetify'
  ],
  publicPath: process.env.NODE_ENV === 'production'
    ? './'
    : '/',
  pages: {
    index: {
      entry: 'src/main.js',
      title: 'SEER'
    }
  },
  devServer: {
    disableHostCheck: true
  }
}
