const gulp = require('gulp');
const del = require('del');


gulp.task('js', function() {
	return gulp.src([
		'node_modules/bootstrap/dist/js/bootstrap.min.js',
		'node_modules/bootstrap/dist/js/bootstrap.min.js.map',
		'node_modules/jquery/dist/jquery.min.js',
		'node_modules/jquery/dist/jquery.min.map',
		'node_modules/select2/dist/js/select2.min.js',
		'node_modules/popper.js/dist/popper.min.js',
		'node_modules/popper.js/dist/popper.min.js.map',
	]).pipe(gulp.dest('vendor/vendor/js'));
}); 

gulp.task('css', function() {
	return gulp.src([
		'node_modules/bootstrap/dist/css/bootstrap.min.css',
		'node_modules/bootstrap/dist/css/bootstrap.min.css.map',
		'node_modules/select2/dist/css/select2.min.css',
	]).pipe(gulp.dest('vendor/vendor/css'));
});


gulp.task('build', gulp.parallel('js', 'css'));

gulp.task('clean', function() {
	return del([
		'vendor/**/*.js',
		'vendor/**/*.css',
	]);

});

gulp.task('default', gulp.series('build'));