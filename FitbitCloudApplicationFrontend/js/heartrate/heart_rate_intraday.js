$(document).ready(function() {
    // Get the token from the sessionStorage
    var access_token = sessionStorage.getItem('access_token');
    console.log("access_token",access_token);

    var urlParams = new URLSearchParams(window.location.search);
    var date = urlParams.get('date');
    // var dateEnd = urlParams.get('endDate');
    console.log('Date:', date);

        // Validate and encode the date
    var datePattern = /^\d{4}-\d{2}-\d{2}$/; // YYYY-MM-DD
    if (!datePattern.test(date) ) {
        console.error('Invalid date format');
        return;
    }
    var encodedDate = encodeURIComponent(date);
    // var encodedDateEnd = encodeURIComponent(dateEnd);


    var table = $('#heartRateIntradayTable').DataTable({
        dom: 'Bfrtip',
        buttons: [
            'copy', 'csv', 'excel', 'pdf', 'print'
        ],
        scrollX: true,
        autoWidth: false,
        deferRender: true, // This will defer the rendering until DataTables is ready to do so
        ajax: {
            url: 'http://localhost:8080/api/heartrate/intraday/' + encodedDate + '/',
            type: 'GET',
            headers: {
                'Authorization': 'Bearer ' + access_token
            },
            dataSrc: 'activities-heart-intraday.dataset',
        },

        columns: [
            { data: 'time', title: 'Time' },
            { data: 'value', title: 'Intraday Heart Rate' },

           
            // Add more columns as needed
        ],
        initComplete: function(settings, json) {
            console.log(json);
        }
    });

    table.columns.adjust().draw();
});