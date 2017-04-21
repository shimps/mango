$(document).ready(function(){
	var fader_box = $('#fader_box');
	var claim_options_box = $('#claim_options_box');
	var right_menu_item = $('#right_menu_item');
	var save_progress_button = $('#save_progress_button_link');
	var claim_form = $('#claim_form');
	
	right_menu_item.on('click',function(){
		fader_box.fadeIn(100);
		claim_options_box.fadeIn(100);
	})
	
	fader_box.on('click',function(){
		claim_options_box.fadeOut(100);
		fader_box.fadeOut(100);
	})
	
	save_progress_button.on('click',function(e){
		e.preventDefault();
		var href = $(this).attr('href');
		claim_form.attr('action',href);
		$('#form_submit_button').click();
		
	})
	
	
})