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


    var table = $('#heartRateVariabilityTable').DataTable({
        scrollX: true,
        autoWidth: false,
        deferRender: true, // This will defer the rendering until DataTables is ready to do so
        ajax: {
            url: 'http://localhost:8080/api/heartrate/variability/' + encodedDate + '/',
            type: 'GET',
            headers: {
                'Authorization': 'Bearer ' + access_token
            },
            dataSrc: function(json) {
                var flattenedData = [];
                json.hrv.forEach(function(item) {
                    item.minutes.forEach(function(minuteItem) {
                        flattenedData.push({
                            minute: minuteItem.minute,
                            value: minuteItem.value
                        });
                    });
                });
                return flattenedData;
            }
        },

        columns: [

            { data: 'minute', title: 'Date Time' },
            { data: 'value.rmssd', title: 'RMS Successive Difference' },
            { data: 'value.coverage', title: 'Coverage in terms of no. of interbeat intervals' },
            { data: 'value.hf', title: 'Interbeat interval fluctuation high frequency(Hz)' },
            { data: 'value.lf', title: 'Interbeat interval fluctuation low frequency(Hz)' }

           
            // Add more columns as needed
        ],
        initComplete: function(settings, json) {
            console.log(json);
        }
    });

    table.columns.adjust().draw();
});