$(document).ready(function(){
	var fader_box = $('#fader_box');
	var policy_apply_button = $('#policy_apply_button');
	var policy_cancel_button = $('#policy_cancel_button');
	var share_button = $('#right_menu_item');
	var policy_options_box = $('#policy_options_box');
	var fader_box = $('#fader_box');
	
	policy_apply_button.on('click',function(){
		$(this).hide();
		policy_cancel_button.show();
	})
	
	policy_cancel_button.on('click',function(){
		$(this).hide();
		policy_apply_button.show();
	})
	
	share_button.on('click',function(){
		fader_box.fadeIn(100);
		policy_options_box.fadeIn(100);
	})
	
	fader_box.on('click',function(){
		policy_options_box.fadeOut(100);
		$(this).fadeOut(100);
	})
	
	
})