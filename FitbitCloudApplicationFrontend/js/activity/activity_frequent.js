$(document).ready(function() {
    // Get the token from the sessionStorage
    var access_token = sessionStorage.getItem('access_token');

    $('#activityFrequentTable').DataTable({
        scrollX: true,

        ajax: {
            url: 'http://localhost:8080/api/activity/frequent_activities/',
            type: 'GET',
            headers: {
                'Authorization': 'Bearer ' + access_token
            },
            dataSrc: 'activities',
            dataFilter: function(data){
                var json = jQuery.parseJSON(data);
                var newjson = {}; 
                newjson.activities = [json];  // Wrap the top-level object in an array and assign it to the 'activities' property
                return JSON.stringify(newjson);
            }

        },
        columns: [


            { data: 'name', title: 'Activity Name' },
            { data: 'calories', title: 'Calories' },
            { data: 'description', title: 'Description' },
            { data: 'distance', title: 'Distance' },
            { data: 'duration', title: 'Duration' },       

           
            // Add more columns as needed
        ],
        initComplete: function(settings, json) {
            console.log(json);
        }
    });
});