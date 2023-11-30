$(document).ready(function() {
    // Get the token from the sessionStorage
    var access_token = sessionStorage.getItem('access_token');
    console.log("access_token",access_token);

    var urlParams = new URLSearchParams(window.location.search);
    var dateStart = urlParams.get('startDate');
    var dateEnd = urlParams.get('endDate');
    console.log('Date:', dateStart,' ',dateEnd);

    // Validate and encode the date
    var datePattern = /^\d{4}-\d{2}-\d{2}$/; // YYYY-MM-DD
    if (!datePattern.test(dateStart) || !datePattern.test(dateEnd)) {
        console.error('Invalid date format');
        return;
    }
    var encodedDateStart = encodeURIComponent(dateStart);
    var encodedDateEnd = encodeURIComponent(dateEnd);
   


    var table = $('#temperatureSkinTable').DataTable({
        dom: 'Bfrtip',
        buttons: [
            'copy', 'csv', 'excel', 'pdf', 'print'
        ],
        scrollX: true,
        autoWidth: false,
        deferRender: true, // This will defer the rendering until DataTables is ready to do so
        ajax: {
            url: 'http://localhost:8080/api/temperature/skin/' + encodedDateStart + '/' + encodedDateEnd + '/',
            type: 'GET',
            headers: {
                'Authorization': 'Bearer ' + access_token
            },
            dataSrc: 'tempSkin'

        },
        columns: [

            { data: 'dateTime', title: 'Date Time' },
            { data: 'logType', title: 'Log Type' },
            { data: 'value.nightlyRelative', title: 'Value reltive to baseline' },


        
            // Add more columns as needed
        ],
        initComplete: function(settings, json) {
            console.log(json);
        }
    });

    table.columns.adjust().draw();
});