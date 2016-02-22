function signInCallback(authResult) {
	if (authResult['code']) {
		$('.google-button').css('display', 'none');
		var state = $('#signInButton').attr('data-state');
		$.ajax({
		    type: 'POST',
		    url: '/gconnect?state=' + state,
		    processData: false,
		    data: authResult['code'],
		    contentType: 'application/octet-stream; charset=utf-8',
		    success: function(result) {
		        // Handle or verify the server response if necessary.
		        if (result) {
		            $('#loginResult').html('Login Successful! ' + result + '. Redirecting...');
		            setTimeout(function() {
		                window.location.href = "/";
		            }, 4000);
		        } else if (authResult['error']) {
		            console.log('There was an error: ' + authResult['error']);
		        } else {
		            console.log('Failed to make a server-side call. Check your configuration and console.');
		        }
	        }
		});
	}
}