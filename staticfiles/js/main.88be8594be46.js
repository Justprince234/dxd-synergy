// set content on click
$('.button').click(function(e) {
    e.preventDefault();
    setContent($(this));
});

// set content on load
$('.button.active').length && setContent($('.button.active'));

function setContent($el) {
    $('.button').removeClass('active');
    $('.container').hide();
    
    $el.addClass('active');
    $($el.data('rel')).show();
};


// set content on click
$('.fashion_category').click(function(event) {
    event.preventDefault();
    setCategory($(this));
});

// set content on load
$('.fashion_category.active').length && setCategory($('.fashion_category.active'));

function setCategory($el) {
    $('.fashion_category').removeClass('active');
    $('.category').hide();
    
    $el.addClass('active');
    $($el.data('rel')).show();
};


// set content on click
$('.delivery').click(function(event) {
    event.preventDefault();
    setCategory($(this));
});

// set content on load
$('.delivery.active').length && setCategory($('.delivery.active'));

function setCategory($el) {
    $('.delivery').removeClass('active');
    $('.delivery_container').hide();
    
    $el.addClass('active');
    $($el.data('rel')).show();
}

$(document).on('click', '#add-button', function (e) {
    e.preventDefault();
    $.ajax({
        type: 'POST',
        url: '{% url "cart:cart_add" %}',
        data: {
            productid: $('#add-button').val(),
            productqty: $('#select option:selected').text(),
            csrfmiddlewaretoken: "{{csrf_token}}",
            action: 'post'
        },
        success: function (json) {
           document.getElementById("cart-quantity").innerHTML = json.quantity
        },
        error: function (xhr, errmsg, err) {}
    });
})


















