/*
$(document).ready(function(){
	console.log("Dentro del JavaScript... 22");
	$("#formUpload").submit(function(event){
		event.preventDefault();
        var formData = $(this).serializeArray();
		console.log(formData);
		var loadingText = "<span class='spinner-border spinner-border-sm' role='status' aria-hidden='true'></span> Procesando...";
		var originalText = "Procesar Archivo";
        var csrftoken = getCookie("csrftoken");
        var csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val();
        console.log("Document Cookie: ", document.cookie);
        console.log("CSRF Middleware token: ", csrfmiddlewaretoken);
        console.log("CSRF Token: ", csrftoken);
		$("#buttonSubmit").prop('disabled', true);
    	if ($("#buttonSubmit").html() !== loadingText) {
    		$("#buttonSubmit").data('original-text', $("#buttonSubmit").html());
    		$("#buttonSubmit").html(loadingText);
    		$("#infoBox").removeClass("d-none");
    	} else {
    		$("#buttonSubmit").data('original-text', $("#buttonSubmit").html());
    		$("#buttonSubmit").html(originalText);
    	}
//        $.ajax({
//            type: "POST",
//            url: 
//        });
    });
});

// ===========================================================
// THIS IS FORM DJANGO DOCUMENTATION TO ENABLE CSRF PROTECTION
// ===========================================================
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});