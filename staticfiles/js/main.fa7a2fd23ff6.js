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

// ***************************************************************************//
// ***************************************************************************//
// ***********************************SIDEBAR SECTION MODIFY STARTS****************************************//
// ***************************************************************************//
// ***************************************************************************//
// ***************************************************************************//
  

function w1_open() {
    document.getElementById("mySidebar").style.width = "100%";
    document.getElementById("mySidebar").style.display = "block";
  }
  
  function w1_close() {
    document.getElementById("mySidebar").style.display = "none";
  };
  
  
  // *************
  function w2_open() {
    document.getElementById("mySidebar2").style.width = "100%";
    document.getElementById("mySidebar2").style.display = "block";
  }
  
  function w2_close() {
    document.getElementById("mySidebar2").style.display = "none";
  };
  
  // *****************
  function w3_open() {
    document.getElementById("mySidebar3").style.width = "100%";
    document.getElementById("mySidebar3").style.display = "block";
  }
  
  function w3_close() {
    document.getElementById("mySidebar3").style.display = "none";
  }
  
  
  // ********************
  function w4_open() {
    document.getElementById("mySidebar4").style.width = "100%";
    document.getElementById("mySidebar4").style.display = "block";
  }
  
  function w4_close() {
    document.getElementById("mySidebar4").style.display = "none";
  }
  
  
  
  
  function w5_open() {
    document.getElementById("mySidebar5").style.width = "100%";
    document.getElementById("mySidebar5").style.display = "block";
  }
  
  function w5_close() {
    document.getElementById("mySidebar5").style.display = "none";
  }
  
  
  // ********************
  function w6_open() {
    document.getElementById("mySidebar6").style.width = "100%";
    document.getElementById("mySidebar6").style.display = "block";
  }
  
  function w6_close() {
    document.getElementById("mySidebar6").style.display = "none";
  }

var form = document.getElementById('sheetdb-form');
form.addEventListener("submit", e=>{ 
    e.preventDefault();
    fetch(form.action, {
        method: "POST",
        body: new FormData(document.getElementById("sheetdb-form")),
    }).then(
        Response => Response.json()
    ).then((html) => {
        alert("Thanks! Your message has been submited!");
    });
    form.reset()
});
// document.getElementById.("myForm").reset();

// Paystack
function payWithPaystack() {
  let currency = 'NGR';
  let plan = "";
  let ref = "{{payment.ref}}";
  let obj = {
    key:"{{paystack_public_key}}",
    email:"{{payment.email}}",
    amount:"{{payment.amount_value}}",
    ref:ref,
    callback: function(response){
      window.location.href="{% url 'payment:verify-payment' payment.ref %}";
    }
  }
  if (Boolean(currency)){
    obj.currency=currency.toUpperCase();
  }
  if (Boolean(plan)){
    obj.plan=plan;
  }
  var handler=PaystackPop.setup(obj);
  handler.openIframe();
}
  
$('#zoom_01').ezPlus();


















