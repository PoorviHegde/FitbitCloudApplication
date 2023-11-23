$(document).ready(function() {
    // Get the token from the sessionStorage
    var access_token = sessionStorage.getItem('access_token');
    console.log(access_token);

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

    var table = $('#bodyWeightTable').DataTable({
        scrollX: true,
        autoWidth: false,
        deferRender: true, // This will defer the rendering until DataTables is ready to do so
        ajax: {
            url: 'http://localhost:8080/api/body/weight/date/' + encodedDate + '/',
            type: 'GET',
            headers: {
                'Authorization': 'Bearer ' + access_token
            },
            dataSrc: function (json) {
                return [json.weight];
            }

        },
        columns: [

            { data: 'bmi', title: 'BMI' },
           
            // Add more columns as needed
        ],
        initComplete: function(settings, json) {
            console.log(json);
        }
    });

    table.columns.adjust().draw();
});