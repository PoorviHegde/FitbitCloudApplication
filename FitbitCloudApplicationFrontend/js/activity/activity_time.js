$(document).ready(function() {
    // Get the token from the sessionStorage
    var access_token = sessionStorage.getItem('access_token');

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

    let flattenedData = [];



    $('#activityTimeTable').DataTable({
        dom: 'Bfrtip',
        buttons: [
            'copy', 'csv', 'excel', 'pdf', 'print'
        ],
        pageLength: 100,
        lengthMenu: [[10, 25, 50, 100, -1], [10, 25, 50, 100, "All"]],
        ajax: {
            url: 'http://localhost:8080/api/activity/time/'+encodedDate+ '/',
            type: 'GET',
            headers: {
                'Authorization': 'Bearer ' + access_token
            },
            dataSrc: 'activities-steps-intraday.dataset',
        },
        columns: [
            { data: 'time', title: 'Time' },
            { data: 'value', title: 'Intraday Steps' }






            //***Need to add Heart Rate Zones columns still ***//
           

           
            // Add more columns as needed
        ],
        initComplete: function(settings, json) {
            console.log(json);
        }
    });
});