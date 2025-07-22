function slider4() {

let splides = $('.slider4');
for ( let i = 0, splideLength = splides.length; i < splideLength; i++ ) {
	new Splide( splides[ i ], {
  // Desktop on down
	perPage: 4,
	perMove: 1,
  focus: 0, // 0 = left and 'center' = center
  type: 'slide', // 'loop' or 'slide'
  gap: '31px', // space between slides
  arrows: 'slider', // 'slider' or false
  pagination: false, // 'slider' or false
  speed : 600, // transition speed in miliseconds
  dragAngleThreshold: 30, // default is 30
  autoWidth: false, // for cards with differing widths
  rewind : false, // go back to beginning when reach end
arrowPath: 'm7.61 0.807-2.12...',
  rewindSpeed : 400,
  waitForTransition : false,
  updateOnMove : true,
  trimSpace: true, // true removes empty space from end of list
  breakpoints: {
		991: {
    	// Tablet
      pagination: false
		},
    767: {
    	// Mobile Landscape
      	perPage: 1,
        pagination: false
		},
    479: {
    	// Mobile Portrait
        perPage: 1,
        pagination: false
		}
	}
} ).mount()};
}
slider4();