$(document).ready(function() {
   
    var $url = $('#id_url');
    var replaceREGEX = /a-z|A-Z|-/gi;
    if(typeof $url != 'undefined' && $url != null) {
	$url.blur(function() {
	    $url.val($url.val().trim().replace(/\s(?!\Z)/g, '-').match(/([0-9a-zA-Z-]+)/g, '').join('').toLowerCase()); 
	});
    }
    
});
