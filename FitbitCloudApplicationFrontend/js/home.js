

$(document).ready(function() {



    $(".collapsible").click(function() {
        $(this).next().slideToggle("slow");
    });

    var access_token = sessionStorage.getItem('access_token');

    if (!access_token || access_token === '[object Object]') {
        $.ajax({
            url: 'http://localhost:8080/get_access_token/',  // Replace with your API endpoint
            type: 'GET',
            success: function(data) {
                // Save the access token in the session storage
                console.log('Data:', data);
                console.log('Access tokenv1:', data.access_token);
                console.log('Access tokenv2:', data.access_token.access_token);
                var access_token = data.access_token;
                sessionStorage.setItem('access_token', access_token.access_token);
            },
            error: function(jqXHR, textStatus, errorThrown) {
                console.error('Error:', textStatus, errorThrown);
            }
        });
    }

    // Initialize the dialog
    $("#datepicker-dialog-actsummary").dialog({
        autoOpen: false,
        width: 100,  // Set the width to 500px
        position: { my: "right", at: "right", of: window }
    });

    // Initialize the dialog
    $("#datepicker-dialog-activtime").dialog({
        autoOpen: false,
        width: 100,  // Set the width to 500px
        position: { my: "right", at: "right", of: window }
    });

    // Initialize the dialog
    $("#datepicker-dialog-bodyfat").dialog({
        autoOpen: false,
        width: 100,  // Set the width to 500px
        position: { my: "right", at: "right", of: window }
    });

    // Initialize the dialog
    $("#datepicker-dialog-weight").dialog({
        autoOpen: false,
        width: 100,  // Set the width to 500px
        position: { my: "right", at: "right", of: window }
    });

    
    // Initialize the dialog
    $("#datepicker-dialog-breathing").dialog({
        autoOpen: false,
        width: 100,  // Set the width to 500px
        position: { my: "right", at: "right", of: window }
    });

    // Initialize the dialog
    $("#datepicker-dialog-cardio").dialog({
        autoOpen: false,
        width: 100,  // Set the width to 500px
        position: { my: "right", at: "right", of: window }
    });

    
    // Initialize the dialog
    $("#datepicker-dialog-hrv").dialog({
        autoOpen: false,
        width: 100,  // Set the width to 500px
        position: { my: "right", at: "right", of: window }
    });

    // Initialize the dialog
    $("#datepicker-dialog-hr").dialog({
        autoOpen: false,
        width: 100,  // Set the width to 500px
        position: { my: "right", at: "right", of: window }
    });

    // Initialize the dialog
    $("#datepicker-dialog-hrintra").dialog({
        autoOpen: false,
        width: 100,  // Set the width to 500px
        position: { my: "right", at: "right", of: window }
    });

        
    // Initialize the dialog
    $("#datepicker-dialog-food").dialog({
        autoOpen: false,
        width: 100,  // Set the width to 500px
        position: { my: "right", at: "right", of: window }
    });

    // Initialize the dialog
    $("#datepicker-dialog-water").dialog({
        autoOpen: false,
        width: 100,  // Set the width to 500px
        position: { my: "right", at: "right", of: window }
    });

    // Initialize the dialog
    $("#datepicker-dialog-oxygen").dialog({
        autoOpen: false,
        width: 100,  // Set the width to 500px
        position: { my: "right", at: "right", of: window }
    });


    // Initialize the dialog
    $("#datepicker-dialog-sleep").dialog({
        autoOpen: false,
        width: 100,  // Set the width to 500px
        position: { my: "right", at: "right", of: window }
    });


    // Initialize the dialog
    $("#datepicker-dialog-sleeplog").dialog({
        autoOpen: false,
        width: 100,  // Set the width to 500px
        position: { my: "right", at: "right", of: window }
    });


     // Initialize the dialog
    $("#datepicker-dialog-temperaturecore").dialog({
        autoOpen: false,
        width: 100,  // Set the width to 500px
        position: { my: "right", at: "right", of: window }
    });


    // Initialize the dialog
    $("#datepicker-dialog-temperatureskin").dialog({
        autoOpen: false,
        width: 100,  // Set the width to 500px
        position: { my: "right", at: "right", of: window }
    });



    // Add a button inside the dialog box
    $("#datepicker-dialog-actsummary").append('<button id="confirm-date-actsummary">Confirm</button>');

    // Add a button inside the dialog box
    $("#datepicker-dialog-activtime").append('<button id="confirm-date-activtime">Confirm</button>');

    // Add a button inside the dialog box
    $("#datepicker-dialog-bodyfat").append('<button id="confirm-date-bodyfat">Confirm</button>');

    // Add a button inside the dialog box
    $("#datepicker-dialog-weight").append('<button id="confirm-date-weight">Confirm</button>');
 
    // Add a button inside the dialog box
    $("#datepicker-dialog-breathing").append('<button id="confirm-date-breathing">Confirm</button>');

    // Add a button inside the dialog box
    $("#datepicker-dialog-cardio").append('<button id="confirm-date-cardio">Confirm</button>');

    // Add a button inside the dialog box
    $("#datepicker-dialog-hrv").append('<button id="confirm-date-hrv">Confirm</button>');

    // Add a button inside the dialog box
    $("#datepicker-dialog-hr").append('<button id="confirm-date-hr">Confirm</button>');

    // Add a button inside the dialog box
    $("#datepicker-dialog-hrintra").append('<button id="confirm-date-hrintra">Confirm</button>');

    // Add a button inside the dialog box
    $("#datepicker-dialog-food").append('<button id="confirm-date-food">Confirm</button>');

    // Add a button inside the dialog box
    $("#datepicker-dialog-water").append('<button id="confirm-date-water">Confirm</button>');

    // Add a button inside the dialog box
    $("#datepicker-dialog-oxygen").append('<button id="confirm-date-oxygen">Confirm</button>');

    
    // Add a button inside the dialog box
    $("#datepicker-dialog-sleep").append('<button id="confirm-date-sleep">Confirm</button>');

        
    // Add a button inside the dialog box
    $("#datepicker-dialog-sleeplog").append('<button id="confirm-date-sleeplog">Confirm</button>');

        
    // Add a button inside the dialog box
    $("#datepicker-dialog-temperaturecore").append('<button id="confirm-date-temperaturecore">Confirm</button>');

        
    // Add a button inside the dialog box
    $("#datepicker-dialog-temperatureskin").append('<button id="confirm-date-temperatureskin">Confirm</button>');

    // Store the picked date in a variable
    var pickedDate;
    $(".datepicker").datepicker({
        onSelect: function(dateText) {
            pickedDate = dateText;
        },
        dateFormat: "yy-mm-dd"
    });

    // Store the picked dates in an array
    var pickedDates = [];
    $(".datepicker_range").datepicker({
        range: 'period', // Enable range selection
        onSelect: function(dateText) {
            pickedDates.push(dateText);
            if (pickedDates.length > 2) {
                // If more than two dates are selected, remove the first one
                pickedDates.shift();
            }
        },
        dateFormat: "yy-mm-dd"
    });

    // When the confirm button is clicked, redirect to the summary page
    $("#confirm-date-actsummary").click(function() {
        if (pickedDate) {
            window.location.href = '../html/activity/activity_summary.html?date=' + encodeURIComponent(pickedDate);
        }
    });

    $("#confirm-date-activtime").click(function() {
        if (pickedDate) {
            window.location.href = '../html/activity/activity_time.html?date=' + encodeURIComponent(pickedDate);
        }
    });


    $("#confirm-date-bodyfat").click(function() {
        if (pickedDate) {
            window.location.href = '../html/body/body_fat.html?date=' + encodeURIComponent(pickedDate);
        }
    });

    $("#confirm-date-weight").click(function() {
        if (pickedDate) {
            window.location.href = '../html/body/body_weight.html?date=' + encodeURIComponent(pickedDate);
        }
    });


    $("#confirm-date-breathing").click(function() {
        if (pickedDates.length === 2) {
            window.location.href = '../html/breathing/breathing.html?startDate=' + encodeURIComponent(pickedDates[0]) + '&endDate=' + encodeURIComponent(pickedDates[1]);
        }
    });


    $("#confirm-date-cardio").click(function() {
        if (pickedDates.length === 2) {
            window.location.href = '../html/cardio/cardio.html?startDate=' + encodeURIComponent(pickedDates[0]) + '&endDate=' + encodeURIComponent(pickedDates[1]);
        }
    });

    $("#confirm-date-hrv").click(function() {
        if (pickedDate) {
            window.location.href = '../html/heartrate/heart_rate_variability.html?date=' + encodeURIComponent(pickedDate);
        }
    });

    $("#confirm-date-hr").click(function() {
        if (pickedDates.length === 2) {
            window.location.href = '../html/heartrate/heart_rate.html?startDate=' + encodeURIComponent(pickedDates[0]) + '&endDate=' + encodeURIComponent(pickedDates[1]);
        }
    });

    
    $("#confirm-date-hrintra").click(function() {
        if (pickedDate) {
            window.location.href = '../html/heartrate/heart_rate_intraday.html?date=' + encodeURIComponent(pickedDate);
        }
    });


    $("#confirm-date-food").click(function() {
        if (pickedDate) {
            window.location.href = '../html/nutrition/food.html?date=' + encodeURIComponent(pickedDate) ;
        }
    });


    $("#confirm-date-water").click(function() {
        if (pickedDate) {
            window.location.href ='../html/nutrition/water.html?date=' + encodeURIComponent(pickedDate) ;
        }
    });


    $("#confirm-date-oxygen").click(function() {
        if (pickedDate) {
            window.location.href ='../html/oxygen/oxygen.html?date=' + encodeURIComponent(pickedDate) ;
        }
    });


    $("#confirm-date-sleep").click(function() {
        if (pickedDates.length === 2) {
            window.location.href = '../html/sleep/sleep.html?startDate=' + encodeURIComponent(pickedDates[0]) + '&endDate=' + encodeURIComponent(pickedDates[1]);
        }
    });


    $("#confirm-date-sleeplog").click(function() {
        if (pickedDate) {
            window.location.href = '../html/sleep/sleeplog.html?date=' + encodeURIComponent(pickedDate) ;
        }
    });

    $("#confirm-date-temperaturecore").click(function() {
        if (pickedDates.length === 2) {
            window.location.href = '../html/temperature/temperature_core.html?startDate=' + encodeURIComponent(pickedDates[0]) + '&endDate=' + encodeURIComponent(pickedDates[1]);
        }
    });

    $("#confirm-date-temperatureskin").click(function() {
        if (pickedDates.length === 2) {
            window.location.href = '../html/temperature/temperature_skin.html?startDate=' + encodeURIComponent(pickedDates[0]) + '&endDate=' + encodeURIComponent(pickedDates[1]);
        }
    });


    // When the "View Activity Summary" link is clicked, open the dialog
    $("#summary_by_date_link").click(function(e) {
        e.preventDefault();
        $("#datepicker-dialog-actsummary").dialog("open");
    });


    // When the "View Activity Summary" link is clicked, open the dialog
    $("#activity_by_time_link").click(function(e) {
        e.preventDefault();
        $("#datepicker-dialog-activtime").dialog("open");
    });


    // When the "View Activity Summary" link is clicked, open the dialog
    $("#body_fat_date_link").click(function(e) {
        e.preventDefault();
        $("#datepicker-dialog-bodyfat").dialog("open");
    });

    
    // When the "View Activity Summary" link is clicked, open the dialog
    $("#body_weight_link").click(function(e) {
        e.preventDefault();
        $("#datepicker-dialog-weight").dialog("open");
    });

    // When the "View Activity Summary" link is clicked, open the dialog
    $("#breathing_link").click(function(e) {
        e.preventDefault();
        $("#datepicker-dialog-breathing").dialog("open");
    });

    $("#breathing_link").click(function(e) {
        e.preventDefault();
        $("#datepicker-dialog-breathing").dialog("open");
    });

    $("#cardio_link").click(function(e) {
        e.preventDefault();
        $("#datepicker-dialog-cardio").dialog("open");
    });

    $("#heart_rate_range").click(function(e) {
        e.preventDefault();
        $("#datepicker-dialog-hr").dialog("open");
    });

    $("#heart_rate_variability").click(function(e) {
        e.preventDefault();
        $("#datepicker-dialog-hrv").dialog("open");
    });

    $("#heart_rate_intraday").click(function(e) {
        e.preventDefault();
        $("#datepicker-dialog-hrintra").dialog("open");
    });


    $("#food_link").click(function(e) {
        e.preventDefault();
        $("#datepicker-dialog-food").dialog("open");
    });

    $("#water_link").click(function(e) {
        e.preventDefault();
        $("#datepicker-dialog-water").dialog("open");
    });

    $("#oxygen_link").click(function(e) {
        e.preventDefault();
        $("#datepicker-dialog-oxygen").dialog("open");
    });

    
    $("#sleep_link").click(function(e) {
        e.preventDefault();
        $("#datepicker-dialog-sleep").dialog("open");
    });

    $("#sleeplog_link").click(function(e) {
        e.preventDefault();
        $("#datepicker-dialog-sleeplog").dialog("open");
    });

    $("#temperature_core_link").click(function(e) {
        e.preventDefault();
        $("#datepicker-dialog-temperaturecore").dialog("open");
    });

    $("#temperature_skin_link").click(function(e) {
        e.preventDefault();
        $("#datepicker-dialog-temperatureskin").dialog("open");
    });

});