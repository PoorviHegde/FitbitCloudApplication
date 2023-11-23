$(document).ready(function() {
    // Get the token from the sessionStorage
    var access_token = sessionStorage.getItem('access_token');

    var urlParams = new URLSearchParams(window.location.search);
    var date = urlParams.get('date');
    console.log('Date:', date);

    // Validate and encode the date
    var datePattern = /^\d{4}-\d{2}-\d{2}$/; // YYYY-MM-DD
    if (!datePattern.test(date)) {
        console.error('Invalid date format');
        return;
    }
    var encodedDate = encodeURIComponent(date);

    $('#activitySummaryTable').DataTable({
        scrollX: true,
        ajax: {
            url: 'http://localhost:8080/api/activity/summary/'+encodedDate+ '/',
            type: 'GET',
            headers: {
                'Authorization': 'Bearer ' + access_token
            },
            dataSrc: function (json) {
                return [json.summary];
            }
        },
        columns: [
            { data: 'activeScore', title: 'Active Score' },
            { data: 'activityCalories', title: 'Active Calories' },
            { data: 'caloriesBMR', title: 'BMR Calories Burned' },
            { data: 'caloriesOut', title: 'Total Calories Burned' },
            { data: 'fairlyActiveMinutes', title: 'Fairly Active' },
            { data: 'lightlyActiveMinutes', title: 'Lightly Active Minutes' },
            { data: 'marginalCalories', title: 'Marginal Calories' },
            { data: 'sedentaryMinutes', title: 'Sedentary Minutes' },
            { data: 'steps', title: 'Steps' },
            { data: 'veryActiveMinutes', title: 'Very Active Minutes' },
            { 
                data: 'distances.0.distance', 
                title: 'Total Distance',
            },
            {  data:'distances.1.distance',title: 'Tracker Distance'},
            { data:'distances.2.distance',  title: 'Logged Activities Distance'},
            { data:'distances.3.distance',title: 'Very Active Distance'},
            { data:'distances.4.distance', title: 'Moderately Activities Distance'},
            { data:'distances.5.distance',title: 'Lightly Active Distance'},
            {  data:'distances.6.distance', title: 'Sedantary Active Distance' },

            {  data:'heartRateZones.0.minutes', title: 'Out of Range Minutes' },
            {  data:'heartRateZones.0.caloriesOut', title: 'Out of Range Calories' },
            {  data:'heartRateZones.1.minutes', title: 'Fat Burn Minutes' },
            {  data:'heartRateZones.1.caloriesOut', title: 'Fat Burn Calories' },
            {  data:'heartRateZones.2.minutes', title: 'Cardio Minutes' },
            {  data:'heartRateZones.2.caloriesOut',title: 'Cardio Calories' },
            {  data:'heartRateZones.3.minutes', title: 'Peak Minutes' },
            {  data:'heartRateZones.3.caloriesOut',title: 'Peak Calories' },






            //***Need to add Heart Rate Zones columns still ***//
           

           
            // Add more columns as needed
        ],
        initComplete: function(settings, json) {
            console.log(json);
        }
    });
});