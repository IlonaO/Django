var gulp = require('gulp');
var sass = require('gulp-sass');
var concat = require('gulp-concat-util');
var webpack = require('webpack');
var postcss = require('gulp-postcss');
var sourcemaps = require('gulp-sourcemaps');
var autoprefixer = require('autoprefixer');
var karma = require('karma');

var paths = {
    karma: __dirname + '/karma.config.js'
};


// Run once tests
gulp.task('test', function (done) {
    process.env.NODE_ENV = 'production';
    new karma.Server({
        configFile: paths.karma,
        singleRun: true
    }, function (karmaExitStatus) {
        if (karmaExitStatus) {
            process.exit(1);
        }
    }).start();
});

// Run once single test
gulp.task('test-single', function (done) {
    process.env.NODE_ENV = 'production';
    new karma.Server({
        configFile: paths.karma,
        files: [__dirname + '/frontend/components/test/industry-state-chooser-spec.js'],
        singleRun: true
    }, function (karmaExitStatus) {
        if (karmaExitStatus) {
            process.exit(1);
        }
    }).start();
});
