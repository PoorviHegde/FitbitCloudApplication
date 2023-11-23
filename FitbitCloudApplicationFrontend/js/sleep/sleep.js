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
   


    var table = $('#sleepTable').DataTable({
        scrollX: true,
        autoWidth: false,
        deferRender: true, // This will defer the rendering until DataTables is ready to do so
        ajax: {
            url: 'http://localhost:8080/api/sleep/' + encodedDateStart + '/' + encodedDateEnd + '/',
            type: 'GET',
            headers: {
                'Authorization': 'Bearer ' + access_token
            },
            dataSrc: 'sleep'

        },
        columns: [

            { data: 'dateOfSleep', title: 'Date' },
            { data: 'duration', title: 'Duration' },
            { data: 'efficiency', title: 'Efficency' },
            { data: 'isMainSleep', title: 'Main Sleep?' },
            { data: 'minutesAfterWakeup', title: 'Minutes After Wake Up' },
            { data: 'minutesAsleep', title: 'Minutes Asleep' },
            { data: 'minutesToFallAsleep', title: 'Minutes To Fall Asleep' },
            { data: 'startTime', title: 'Start Time' },
            { data: 'endTime', title: 'End Time' },
            { data: 'timeInBed', title: 'Time In Bed(Minutes)' },

        
            // Add more columns as needed
        ],
        initComplete: function(settings, json) {
            console.log(json);
        }
    });

    table.columns.adjust().draw();
});