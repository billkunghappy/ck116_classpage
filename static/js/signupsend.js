$(document).ready(function () {	
	$( "#sign_button" ).click(function() {
		  	var sign_name = $("#sign_name").val();
			var sign_pw = $("#sign_pw").val();
			var sign_v_pw = $("#sign_v_pe").val();
			var sign_email = $("#sign_email").val();
			// window.location = 'signupenter.html?
			// 					sign_name='+ sign_name +
			// 					',sign_pw='+ sign_pw +
			// 					',sign_v_pw='+ sign_v_pw +
			// 					',sign_email='+sign_email ;
			window.location.href = "http://www.sitepoint.com/url-parameters-jquery/?sign_name=" + sign_name + "&sign_pw=" + sign_pw + "&sign_v_pw=" + sign_v_pw + "&sign_email=" + sign_email;
			return false;
		});
}