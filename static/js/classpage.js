$(document).ready(function () {
    if ($('#name').is(':empty')){
    	$('#name').hide();
	}
	else {
		$('#name').show().delay(5000).fadeOut();
	}

	if ($('#password').is(':empty')){
    	$('#password').hide();
	}
	else {
		$('#password').show().delay(5000).fadeOut();
	}

	if ($('#v_password').is(':empty')){
    	$('#v_password').hide();
	}
	else {
		$('#v_password').show().delay(5000).fadeOut();
	}

	if ($('#email').is(':empty')){
    	$('#email').hide();
	}
	else {
		$('#email').show().delay(5000).fadeOut();
	}

	if ($('#error').is(':empty')){
    	$('#error').hide();
	}
	else {
		$('#error').show();
	}
	
	
});