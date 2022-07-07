
        $(document).ready(function () {
            $("#myCarousel").carousel({
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
            $("#myCarousel11").carousel({
                interval: false
            });
            $("#myCarousel12").carousel({
                interval: false
            });
            $("#myCarousel13").carousel({
                interval: false
            });
            $("#myCarousel14").carousel({
                interval: false
            });
            $("#myCarousel15").carousel({
                interval: false
            });
        });






        const Toast = Swal.mixin({
            toast: true,
            position: 'top-end',
            showConfirmButton: false,
            timer: 3000,
            timerProgressBar: true,
            didOpen: (toast) => {
              toast.addEventListener('mouseenter', Swal.stopTimer)
              toast.addEventListener('mouseleave', Swal.resumeTimer)
            }
          })
          
          Toast.fire({
            icon: 'success',
            title: 'Signed in successfully'
          })