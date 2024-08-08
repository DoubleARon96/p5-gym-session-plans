var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();
var card = elements.create("card");
card.mount('#card-element');

card.addEventListener('change', function (event){
    var errorDiv = document.getElementById('card-errors');
    if (event.error){
        var html = 
        `<span class="icon" role="alet">
            <i class="fas fa-times"></i>
        </span>
        <span>${event.error.message}</span>
        `
        $(errorDiv).html(html);
    }else{
        errorDiv.textContent = '';
    }
});


// submit button function
var form = document.getElementById('payment_form');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    card.update({ 'disabled': true});
    $('#submit-button').attr('disabled', true);

    var saveInfo = Boolean($('#id-save-info').attr('checked'));
    var csrfToken = $('input[name=csrfmiddlewaretoken]').val();
    var postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret':clientSecret,
        'save_info':saveInfo
    }
    var url = '/payment/cache_payment_data/';
    $.post(url, postData).done(function(){

        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
                billing_details:{
                    full_name:$trim(form.full_name.value),
                    email:$trim(form.email.value),
                    phone_number:$trim(form.phone_number.value),
                    country:$trim(form.country.value),
                    town_or_city:$trim(form.country.value),
                    first_line_of_address:$trim(form.country.value),
                    second_line_of_address:$trim(form.country.value),
                    county:$trim(form.country.value),
    
                },
                shipping_details:{
                    name: $trim(form.full_name.value),
                    phone: $trim(form.phone_number.value),
                    country: $trim(form.country.value),
                    post_code: $trim(form.country.value),
                    town_or_city: $trim(form.country.value),
                    first_line_of_address: $trim(form.country.value),
                    second_line_of_address: $trim(form.country.value),
                    county:$trim(form.country.value),
    
                }
            }
        }).then(function(result) {
            if (result.error) {
                var errorDiv = document.getElementById('card-errors');
                var html = `
                    <span class="icon" role="alert">
                    <i class="fas fa-times"></i>
                    </span>
                    <span>${result.error.message}</span>`;
                $(errorDiv).html(html);
                card.update({ 'disabled': false});
                $('#submit-button').attr('disabled', false);
            } else {
                if (result.paymentIntent.status === 'succeeded') {
                    form.submit();
                }
            }
        });
    }).fail(function(){
        location.reload();

    })
        
    });

    /**stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
            billing_details:{
                full_name:$trim(form.full_name.value),
                email:$trim(form.email.value),
                phone_number:$trim(form.phone_number.value),
                country:$trim(form.country.value),
                town_or_city:$trim(form.country.value),
                first_line_of_address:$trim(form.country.value),
                second_line_of_address:$trim(form.country.value),
                county:$trim(form.country.value),

            },
            shipping_details:{
                name: $trim(form.full_name.value),
                phone: $trim(form.phone_number.value),
                country: $trim(form.country.value),
                post_code: $trim(form.country.value),
                town_or_city: $trim(form.country.value),
                first_line_of_address: $trim(form.country.value),
                second_line_of_address: $trim(form.country.value),
                county:$trim(form.country.value),

            }
        }
    }).then(function(result) {
        if (result.error) {
            var errorDiv = document.getElementById('card-errors');
            var html = `
                <span class="icon" role="alert">
                <i class="fas fa-times"></i>
                </span>
                <span>${result.error.message}</span>`;
            $(errorDiv).html(html);
            card.update({ 'disabled': false});
            $('#submit-button').attr('disabled', false);
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
});*/