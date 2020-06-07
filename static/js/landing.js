$(document).ready(function(){
    $('#submit').hide();
    $('#findAddress').click(function(){
        $('#postcode-error').remove();
        $.get('/postcode/' + $('#postcode').val().replace(/\s+/g, ''), function(data, textStatus, jqXHR) {
            var addresses = JSON.parse(data);
            if (addresses.length == 0) {
                $('#postcode-group').append('<span id="postcode-error" style="color: darkred;">No addresses were found for your postcode. Please add your address manually in the emails.</span>');
                $('#address').prop('required', false);
            }
            else {
                for (i = 0; i < addresses.length; i++) {
                    $('#address').append('<option>' + addresses[i] + '</option>');
                    $('#address-group').show();
                }
            }
            $('#findAddress').hide();
            $('#postcode').hide();
            $('#submit').show();
        }).fail(function() {
            $('#postcode-group').append('<span id="postcode-error" style="color: darkred;">Invalid postcode. Please try again.</span>');
        });
    });
});