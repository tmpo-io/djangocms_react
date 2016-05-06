
var gulp = require('gulp');
var browserify = require('browserify');
var source = require('vinyl-source-stream');
var gutil = require('gulp-util');
var babelify = require('babelify');
var sass = require('gulp-sass');
var plumber = require('gulp-plumber')

var js_path = "../js/"
var css_path = "../css/"

gulp.task('scripts', function () {

  var appBundler = browserify({
  	entries: './app/app.js',
  	debug: true
  })

  browserify({
    require: [
    	'react',
      'react-dom'
    ],
    debug: true
  })
  .bundle()
  .on('error', gutil.log)
  .pipe(source('vendors.js'))
  .pipe(gulp.dest(js_path));

  appBundler
  	.transform("babelify", {presets: ["es2015", "react"]})
    .bundle()
    .on('error',gutil.log)
    .pipe(source('bundle.js'))
    .pipe(gulp.dest(js_path));
});

gulp.task('sass', function() {
    return gulp.src('scss/main.scss')
        .pipe(plumber({
            errorHandler: function (err) {
              gutil.beep();
              gutil.log( gutil.colors.red( err ) );
              this.emit('end');
            }
        }))
        .pipe(sass({includePaths: [
            './',
            './bower_components/'
        ]}))
        .pipe(gulp.dest(css_path))
});

gulp.task('watch', function () {
  gulp.watch('scss/**/*.scss', ['sass']);
	gulp.watch(['./app/*.js'], ['scripts']);
});

gulp.task('default', ['scripts','watch']);
