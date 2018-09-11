var gulp = require('gulp');
var karma = require('karma');

var paths = {
    karma: __dirname + '/karma.config.js'
};

gulp.task('test', function (done) {
    new karma.Server({
        configFile: paths.karma,
        singleRun: true
    }, function (karmaExitStatus) {
        if (karmaExitStatus) {
            process.exit(1);
        }
    }).start();
});

gulp.task('single-test', function (done) {
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
