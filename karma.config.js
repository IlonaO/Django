var webpackConfig = require('./webpack.config.js');

module.exports = function (config) {
    config.set({
        basePath: '',
        frameworks: ['jasmine'],
        reporters: ['progress', 'coverage'],
        port: 9876,
        colors: false,
        logLevel: config.LOG_INFO,
        autoWatch: true,
        singleRun: true,
        autoWatchBatchDelay: 300,

        browserDisconnectTimeout: 2000, // default 2000
        browserDisconnectTolerance: 1, // default 0
        browserNoActivityTimeout: 40000, //default 10000

        files: [
            // './frontend/config_test.js',
            './frontend/index.js',
            './frontend/components/*.vue',
            './frontend/components/test/*-spec.js'
        ],

        preprocessors: {
            './frontend/components/*.vue': ['webpack', 'coverage'],
            './frontend/index.js': ['webpack', 'coverage'],
            './frontend/components/test/*-spec.js': ['webpack']
        },


        coverageReporter: {
            dir: 'statics/test/coverage/',
            reporters: [
                {type: 'text-summary'},
                {type: 'html'}
            ]
        },

        browsers: ['ChromeHeadless'],
        customLaunchers: {
            ChromeHeadless: {
                base: 'Chrome',
                flags: ['--no-sandbox', '--headless', '--disable-gpu', '--remote-debugging-port=9222']
            }
        },
        webpack: webpackConfig,
        webpackMiddleware: {
            noInfo: true
        }

    });
};
