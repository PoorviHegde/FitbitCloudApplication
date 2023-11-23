$(document).ready(function() {
    // Get the token from the sessionStorage
    var access_token = sessionStorage.getItem('access_token');
    console.log("access_token",access_token);

    var urlParams = new URLSearchParams(window.location.search);
    var date = urlParams.get('date');

    console.log('Date:', date);

        // Validate and encode the date
    var datePattern = /^\d{4}-\d{2}-\d{2}$/; // YYYY-MM-DD
    if (!datePattern.test(date) ) {
        console.error('Invalid date format');
        return;
    }
    var encodedDateStart = encodeURIComponent(date);
   


    var table = $('#oxygenTable').DataTable({
        scrollX: true,
        autoWidth: false,
        deferRender: true, // This will defer the rendering until DataTables is ready to do so
        ajax: {
            url: 'http://localhost:8080/api/oxygen/' + encodedDateStart + '/',
            type: 'GET',
            headers: {
                'Authorization': 'Bearer ' + access_token
            },
            dataSrc: function (json) {
                return [json];
            }

        },
        columns: [

            { data: 'dateTime', title: 'Date Time' },
            { data: 'value.avg', title: 'Average' },
            { data: 'value.min', title: 'Minimum' },
            { data: 'value.max', title: 'Maximum' },

        
            // Add more columns as needed
        ],
        initComplete: function(settings, json) {
            console.log(json);
        }
    });

    table.columns.adjust().draw();
});