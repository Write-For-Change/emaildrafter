$(document).ready(function(){
    $('#submit').hide();
    $('#id_address').hide();
    $('label[for="id_address"]').hide();
    $('#id_constituency').hide();
    $('label[for="id_constituency"]').hide();
    $('#findAddress').click(function(){
        $('#postcode-error').remove();
        $.get('/postcode/' + $('#id_postcode').val().replace(/\s+/g, ''), function(data, textStatus, jqXHR) {
            // Valid JSON returned by Django so do not need to parse since jQuery handles it
            // var response = JSON.parse(data);
            var addresses = data.addresses;
            var constituency = data.constituency;
            if (addresses.length == 0) {
                $('#postcode-group').append('<span id="postcode-error" style="color: darkred;">No addresses were found for your postcode. Please add your address manually in the emails.</span>');
                $('#id_address').prop('required', false);
            }
            else {
                for (i = 0; i < addresses.length; i++) {
                    $('#id_address').append('<option>' + addresses[i] + '</option>');
                    $('#id_address').show();
                }
                $('#id_constituency').val(constituency);


            }
            $('#findAddress').hide();
            $('#id_postcode').hide();
            $('#submit').show();
        }).fail(function() {
            $('#postcode-group').append('<span id="postcode-error" style="color: darkred;">Invalid postcode. Please try again.</span>');
        });
    });
});
