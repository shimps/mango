$(document).ready(function(){
	var fader_box = $('#fader_box');
	var application_options_box = $('#application_options_box');
	var right_menu_item = $('#right_menu_item');
	var application_form = $('#application_form');
	var save_progress_button = $('#save_progress_button_link');
	
	
	right_menu_item.on('click',function(){
		fader_box.fadeIn(100);
		application_options_box.fadeIn(100);
	})
	
	fader_box.on('click',function(){
		application_options_box.fadeOut(100);
		fader_box.fadeOut(100);
	})
	
	
	save_progress_button.on('click',function(e){
		e.preventDefault();
		var href = $(this).attr('href');
		application_form.attr('action',href);
		console.log(application_form.attr('action'))
		$('#form_submit_button').click();
		
	})
})