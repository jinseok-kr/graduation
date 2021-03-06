const FileManagerPlugin = require('filemanager-webpack-plugin-fixed'); //파일메니저 플러그인을 import 시키는 코드


module.exports = {
  transpileDependencies: [
    'vuetify'
  ],

  devServer: {
    index: 'home.html',
    proxy: 'http://127.0.0.1:8000',
  },

  outputDir: 'dist',
  publicPath: '/',
  assetsDir: 'static',


  pages:{
    home: {
      template: 'public/index.html',
      entry: 'src/pages/main_home.js',
      filename: 'home.html',
      title: '뉴스와 친해지자',
      minify: false,
    },
    post_list: {
      template: 'public/index.html', 
      entry: 'src/pages/main_post_list.js', 
      filename: 'post_list.html', 
      title: '뉴스와 친해지자-post list', 
      minify: false, 
    },
    post_detail:{
      template: 'public/index.html', 
      entry: 'src/pages/main_post_detail.js', 
      filename: 'post_detail.html', 
      title: '뉴스와 친해지자', 
      minify: false, 
    },
    post_scrap: {
      template: 'public/index.html', 
      entry: 'src/pages/main_post_scrap.js', 
      filename: 'post_scrap.html', 
      title: '뉴스와 친해지자-post scrap', 
      minify: false, 
    },
    news_list: {
      template: 'public/index.html', 
      entry: 'src/pages/main_news_list.js', 
      filename: 'news_list.html', 
      title: '뉴스와 친해지자-news list', 
      minify: false, 
    },
    news_detail:{
      template: 'public/index.html', 
      entry: 'src/pages/main_news_detail.js', 
      filename: 'news_detail.html', 
      title: '뉴스와 친해지자', 
      minify: false, 
    },
    news_scrap: {
      template: 'public/index.html', 
      entry: 'src/pages/main_news_scrap.js', 
      filename: 'news_scrap.html', 
      title: '뉴스와 친해지자-news scrap', 
      minify: false, 
    },
  },

  
  configureWebpack: {
    plugins: [
      new FileManagerPlugin({
        onStart: {
          delete: [
            '../backend/static/**/',
            '../backend/templates/**/',
          ],
        },

        onEnd: {
          copy: [
            { source: 'dist/static', destination: '../backend/static/' },
            { source: 'dist/favicon.ico', destination: '../backend/static/img/' },
            { source: 'dist/home.html', destination: '../backend/templates/' },
            { source: 'dist/post*.html', destination: '../backend/templates/blog/' },
            { source: 'dist/news*.html', destination: '../backend/templates/blog/' },
          ],
        }
      }),
    ]    
  },
}
