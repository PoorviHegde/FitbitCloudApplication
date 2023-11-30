$(document).ready(function() {
    // Get the token from the sessionStorage
    var access_token = sessionStorage.getItem('access_token');
    console.log("access_token",access_token);

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


    var table = $('#sleepLogTable').DataTable({
        dom: 'Bfrtip',
        buttons: [
            'copy', 'csv', 'excel', 'pdf', 'print'
        ],
        scrollX: true,
        autoWidth: false,
        deferRender: true, // This will defer the rendering until DataTables is ready to do so
        ajax: {
            url: 'http://localhost:8080/api/sleeplog/' + encodedDate + '/',
            type: 'GET',
            headers: {
                'Authorization': 'Bearer ' + access_token
            },
            dataSrc: function(json) {
                var flattenedData = [];
                json.sleep.forEach(function(item) {
                    var durationInMinutes = (item.duration / 60000).toFixed(2); // rounds to 2 decimal places
                    item.levels.data.forEach(function(dataItem) {
                        flattenedData.push({
                            datetime: dataItem.dateTime,
                            level: dataItem.level
                        });
                    });
                    item.levels.shortData.forEach(function(shortdataItem) {
                        flattenedData.push({
                            datetime: shortdataItem.dateTime,
                            level: shortdataItem.level
                        });
                    });
                });
                return flattenedData;
            }

        },
        columns: [

            { data: 'datetime', title: 'Date Time' },
            { data: 'level', title: 'Level' }

        
            // Add more columns as needed
        ],
        initComplete: function(settings, json) {
            console.log(json);
        }
    });

    table.columns.adjust().draw();
});