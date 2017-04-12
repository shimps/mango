$(document).ready(function(){
	var fader_box = $('#fader_box');
	var signup_button = $('#signup_button');
	var main_page_login_button = $('#main_page_login_button');
	var account_options_box = $('#account_options_box');
	var account_options_button = $('#account_options_button');
	var login_box = $('#login_box');
	var login_form = $('#login_form');
	var login_button = $('#login_button');
	
	signup_button.on('click',function(){
		fader_box.fadeIn(100);
		account_options_box.fadeIn(100);
	})
	
	main_page_login_button.on('click',function(){
		fader_box.fadeIn(100);
		login_box.fadeIn(100);
	})
	
	fader_box.on('click',function(){
		account_options_box.fadeOut(100);
		login_box.fadeOut(100);
		fader_box.fadeOut(100);
	})
	
})