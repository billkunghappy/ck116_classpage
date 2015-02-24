$( "#login_button" ).click(function() {
		var login_name = $("#login_name").val();
		var login_pw = $("#login_pw").val();

		$("#login_var1").val(login_name);
		$("#login_var2").val(login_pw);
		$("#loginform").submit();
	});