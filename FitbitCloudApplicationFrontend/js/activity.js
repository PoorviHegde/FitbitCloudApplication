$(document).ready(function() {
    $(".collapsible").click(function() {
        $(this).next().slideToggle("slow");
    });
});