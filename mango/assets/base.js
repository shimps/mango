$(document).ready(function(){
	var fader_box = $('#fader_box');
	var side_menu  = $('#side_menu');
	
	$('#left_menu_item').on('click',function(){
		side_menu.fadeIn(200);
		fader_box.fadeIn(200);
	})
	
	fader_box.on('click',function(){
		side_menu.fadeOut(200);
		fader_box.fadeOut(200);
	})
})
