var path = require('path');
var webpack = require('webpack');
var ExtractTextPlugin = require("extract-text-webpack-plugin");
var extract_css = new ExtractTextPlugin("css/[name].css");
var BundleTracker = require('webpack-bundle-tracker');

module.exports = {
  plugins: [new BundleTracker({filename: './webpack-stats.json'}), extract_css],
  entry: {
    vue: './frontend/index.js',
    //base: './frontend/main.sass'
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
        loader: 'vue-loader',
        options: {
          loaders: {
            'scss': ExtractTextPlugin.extract({
              use: [
                {loader: 'css-loader', options: {sourceMap: true}},
                {loader: 'sass-loader', options: {sourceMap: true}},
                {loader: 'postcss-loader', options: {sourceMap: true}}
              ],
              fallback: 'vue-style-loader'
            }),
            'sass': ExtractTextPlugin.extract({
              use: [
                {loader: 'css-loader', options: {sourceMap: true}},
                {loader: 'sass-loader', options: {indentedSyntax: true, sourceMap: true}},
                {loader: 'postcss-loader', options: {sourceMap: true}}
              ],
              fallback: 'vue-style-loader'
            })
          }
        }
      },
      {
        test: /\.sass$/,
        loader: ExtractTextPlugin.extract({fallback: 'vue-style-loader', use:'css-loader!sass-loader?indentedSyntax!import-glob-loader'}), //# postcss-loader'),
          exclude: /node_modules/
      },
      {
        test: /\.js$/,
        loader: 'babel-loader?cacheDirectory',
        exclude: /node_modules\/(?!(dom7|swiper)\/).*/,
      },
      {
        test: /\.(png|jpg|gif|svg)$/,
        loader: 'file-loader',
        options: {
          name: '[name].[ext]?[hash]'
        }
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
