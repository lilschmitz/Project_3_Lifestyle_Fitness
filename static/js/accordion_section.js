$(document).ready(function() {
	"use strict";

	var $close = $('header #closePanel');

	//List Item Click
	$('.accordion .accordion-control').on('click', function(e){
	  // e.Default('open');
		$(this).parent().toggleClass();
		$(this).toggleClass();

		$(this).next('.accordion-panel').slideToggle();
	});


	//Close Button Click
	$close.on('click', function(e){
		// e.preventDefault();


	}); // end close click


});




