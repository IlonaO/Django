var path = require('path');
var webpack = require('webpack');
var ExtractTextPlugin = require("extract-text-webpack-plugin");
var extract_css = new ExtractTextPlugin("css/[name].css");
var BundleTracker = require('webpack-bundle-tracker');

module.exports = {
  plugins: [new BundleTracker({filename: './webpack-stats.json'}), extract_css],
  entry: {
    vue: './frontend/index.js'
  },
  output: {
    path: path.resolve(__dirname, './statics'),
    publicPath: '/statics',
    filename: 'js/[name].js'
  },
  module: {
    rules: [
      {
        test: /\.vue$/,
        loader: 'vue-loader'
      },
      {
        test: /\.scss$/,
        use: [
          'vue-style-loader',
          'css-loader',
          'sass-loader'
        ]
      },
      {
        test: /\.js$/,
        exclude: /node_modules\/(?!(dom7|swiper)\/).*/,
        loader: 'babel-loader'
      }
    ]
  },
  resolve: {
    alias: {
      'vue$': 'vue/dist/vue.esm.js'
    }
  },
  performance: {
    hints: false
  },
  cache: true,
  devtool: '#eval-source-map'
};
