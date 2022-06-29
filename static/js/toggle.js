function toggleText() {

    // Get all the elements from the page
    var points =
        document.getElementById("points");

    var showMoreText =
        document.getElementById("moreText");

    var buttonText =
        document.getElementById("textButton");

    // If the display property of the dots 
    // to be displayed is already set to 
    // 'none' (that is hidden) then this 
    // section of code triggers
    if (points.style.display === "none") {

        // Hide the text between the span
        // elements
        showMoreText.style.display = "none";

        // Show the dots after the text
        points.style.display = "inline";

        // Change the text on button to 
        // 'Show More'
        buttonText.innerHTML = "Show More";
    }

    // If the hidden portion is revealed,
    // we will change it back to be hidden
    else {

        // Show the text between the
        // span elements
        showMoreText.style.display = "inline";

        // Hide the dots after the text
        points.style.display = "none";

        // Change the text on button
        // to 'Show Less'
        buttonText.innerHTML = "Show Less";
    }
};



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