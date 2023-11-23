$(document).ready(function() {
    // Get the token from the sessionStorage
    var access_token = sessionStorage.getItem('access_token');

    $('#activityLogTable').DataTable({
        scrollX: true,
        ajax: {
            url: 'http://localhost:8080/api/activity/log/',
            type: 'GET',
            headers: {
                'Authorization': 'Bearer ' + access_token
            },
            dataSrc: 'activities'
        },
        columns: [
            { data: 'activityName', title: 'Activity Name' },
            { 
                data: 'activeDuration', 
                title: 'Active Duration(mins)',
                render: function(data, type, row) {
                    return (data / 60000).toFixed(2); // divide by 60000 to convert milliseconds to minutes
                }
            },
            
            { data: 'calories', title: 'Calories Burned' },
            { data: 'duration', title: 'Duration',
            render: function(data, type, row) {
                return (data / 60000).toFixed(2); // divide by 60000 to convert milliseconds to minutes
            } },
            {  title: 'Minutes in Peak zone',               
             render: function(data, type, row) {
                return row.activeZoneMinutes.minutesInHeartRateZones[0].minutes;// divide by 60000 to convert milliseconds to minutes
            } },
            {  title: 'Minutes in Cardio zone',
            render: function(data, type, row) {
                return row.activeZoneMinutes.minutesInHeartRateZones[1].minutes;// divide by 60000 to convert milliseconds to minutes
            } },
            {  title: 'Minutes in FatBurn zone',
            render: function(data, type, row) {
                return row.activeZoneMinutes.minutesInHeartRateZones[2].minutes; // divide by 60000 to convert milliseconds to minutes
            } },
            { title: 'Minutes in OutOfRange zone',
            render: function(data, type, row) {
                return row.activeZoneMinutes.minutesInHeartRateZones[3].minutes; // divide by 60000 to convert milliseconds to minutes
            } },
            {  title: 'Activity Minutes:Sedentary',        
            render: function(data, type, row) {
                return row.activityLevel[0].minutes;
            }},
            {  title: 'Activity Minutes:Lightly ',
            render: function(data, type, row) {
                return row.activityLevel[1].minutes;
            }},
            { title: 'Activity Minutes:Fairly',
            render: function(data, type, row) {
                return row.activityLevel[2].minutes;
            } },
            {  title: 'Activity Minutes:Very',
            render: function(data, type, row) {
                return row.activityLevel[3].minutes;
            } },

            { data: 'lastModified', title: 'Last Modified' },
            { data: 'logType', title: 'Log Type' },

           
            // Add more columns as needed
        ],
        initComplete: function(settings, json) {
            console.log(json);
        }
    });
});