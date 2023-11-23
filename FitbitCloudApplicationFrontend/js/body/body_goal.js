$(document).ready(function() {
    // Get the token from the sessionStorage
    var access_token = sessionStorage.getItem('access_token');
    console.log(access_token);

    var table = $('#bodyGoalTable').DataTable({
        scrollX: true,
        autoWidth: false,
        deferRender: true, // This will defer the rendering until DataTables is ready to do so
        ajax: {
            url: 'http://localhost:8080/api/body/goal/',
            type: 'GET',
            headers: {
                'Authorization': 'Bearer ' + access_token
            },
            dataSrc: function (json) {
                return [json.goal];
            }

        },
        columns: [

            { data: 'goalType', title: 'Goal Type' },
            { data: 'startDate', title: 'Start Date' },
            { data: 'startWeight', title: 'Start Weight' },
            { data: 'weight', title: 'Weight' },
            { data: 'weightThreshold', title: 'Weight Threshold' },

           
            // Add more columns as needed
        ],
        initComplete: function(settings, json) {
            console.log(json);
        }
    });

    table.columns.adjust().draw();
});