$(document).ready(function(){
	var policy_apply_button = $('#policy_apply_button');
	var policy_cancel_button = $('#policy_cancel_button');
	
	policy_apply_button.on('click',function(){
		$(this).hide();
		policy_cancel_button.show();
	})
	
	policy_cancel_button.on('click',function(){
		$(this).hide();
		policy_apply_button.show();
	})
	
})