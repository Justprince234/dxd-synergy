
        $(document).ready(function () {
            $("#myCarousel").carousel({
                interval: false
            });
            $("#myCarousel1").carousel({
                interval: false
            });
            $("#myCarousel2").carousel({
                interval: false
            });
            $("#myCarousel3").carousel({
                interval: false
            });
            $("#myCarousel4").carousel({
                interval: false
            });
            $("#myCarousel5").carousel({
                interval: false
            });
            $("#myCarousel6").carousel({
                interval: false
            });
            $("#myCarousel7").carousel({
                interval: false
            });
            $("#myCarousel8").carousel({
                interval: false
            });
            $("#myCarousel9").carousel({
                interval: false
            });
            $("#myCarousel10").carousel({
                interval: false
            });
        });




        
        // *************************SWEET ALERT****************************************//
        

        document.querySelector(".first").addEventListener('click', function (event){
            event.preventDefault();
            swal({
                title: "Success!",
                text: "Succesfully added item to cart",
                type: "success",
                timer: 1000,
                showConfirmButton: false
              })
        });

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
                   document.getElementById("basket-qty").innerHTML = json.quantity
                },
                error: function (xhr, errmsg, err) {}
            });
        })
