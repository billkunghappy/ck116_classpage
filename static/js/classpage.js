$(document).ready(function () {
    if ($('#name').is(':empty')){
    	$('#name').hide();

	}
	else {
		$('#name').show()
		$('#signup').modal('show');
	}

	if ($('#password').is(':empty')){
    	$('#password').hide();
	}
	else {
		$('#password').show();
		$('#signup').modal('show');
	}

	if ($('#v_password').is(':empty')){
    	$('#v_password').hide();
	}
	else {
		$('#v_password').show();
		$('#signup').modal('show');
	}

	if ($('#email').is(':empty')){
    	$('#email').hide();
	}
	else {
		$('#email').show();
		$('#signup').modal('show');
	}

	if ($('#error').is(':empty')){
    	$('#error').hide();
    	$('#signup_btn').show();
		$('#login_btn').show();
		$('#logout_btn').hide();
	}
	else {
		$('#error').show();
		$('#signup_btn').hide();
		$('#login_btn').hide();
		$('#logout_btn').show();
	}
// login down
	if ($('#login_name_error').is(':empty')){
    	$('#login_name_error').hide();
	}
	else {
		$('#login_name_error').show()
		$('#login').modal('show');
	}

	if ($('#login_pw_error').is(':empty')){
    	$('#login_pw_error').hide();
	}
	else {
		$('#login_pw_error').show();
		$('#login').modal('show');
	}
	if ($('#login_error').is(':empty')){
    	$('#login_error').hide();

	}
	else {
		$('#login_error').show();
		$('#signup_btn').hide();

	}
	$('#yes').show();
	$('#false').hide();
	$('#yesimage').hide();
	$('#falseimage').show();
	
});