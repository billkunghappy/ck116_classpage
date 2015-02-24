$( "#sign_button" ).click(function() {
		var sign_name = $("#sign_name").val();
		var sign_pw = $("#sign_pw").val();
		var sign_v_pw = $("#sign_v_pw").val();
		var sign_email = $("#sign_email").val();
			// window.location = 'signupenter.html?
			// 					sign_name='+ sign_name +
			// 					',sign_pw='+ sign_pw +
			// 					',sign_v_pw='+ sign_v_pw +
			// 					',sign_email='+sign_email ;
			// window.location.href = "/signuptest/?sign_name=" + sign_name + "&sign_pw=" + sign_pw + "&sign_v_pw=" + sign_v_pw + "&sign_email=" + sign_email;
		$("#var1").val(sign_name);
		$("#var2").val(sign_pw);
		$("#var3").val(sign_v_pw);
		$("#var4").val(sign_email);
		$("#signform").submit();
	});
