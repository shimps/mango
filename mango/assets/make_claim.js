$(document).ready(function(){
	var fader_box = $('#fader_box');
	var claim_options_box = $('#claim_options_box');
	var right_menu_item = $('#right_menu_item');
	
	right_menu_item.on('click',function(){
		fader_box.fadeIn(100);
		claim_options_box.fadeIn(100);
	})
	
	fader_box.on('click',function(){
		claim_options_box.fadeOut(100);
		fader_box.fadeOut(100);
	})
	
	
})