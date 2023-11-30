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


    var table = $('#heartRateTable').DataTable({
        dom: 'Bfrtip',
        buttons: [
            'copy', 'csv', 'excel', 'pdf', 'print'
        ],
        scrollX: true,
        autoWidth: false,
        deferRender: true, // This will defer the rendering until DataTables is ready to do so
        ajax: {
            url: 'http://localhost:8080/api/heartrate/' + encodedDateStart + '/' + encodedDateEnd + '/',
            type: 'GET',
            headers: {
                'Authorization': 'Bearer ' + access_token
            },
            dataSrc: 'activities-heart'

        },
        columns: [

            { data: 'dateTime', title: 'Date Time' },
            {  render: function(data, type, row) {return row.value.heartRateZones[0].max}, title: 'Out of Range Max' },
            { render: function(data, type, row) {return row.value.heartRateZones[0].min}, title: 'Out of Range Min' },
            { render: function(data, type, row) {return parseFloat(row.value.heartRateZones[0].caloriesOut.toFixed(2))}, title: 'Out of Range Calories' },
            { render: function(data, type, row) {return row.value.heartRateZones[0].minutes}, title: 'Out of Range Minutes' },
            { render: function(data, type, row) {return row.value.heartRateZones[1].max}, title: 'Fat Burn Max' },
            { render: function(data, type, row) {return row.value.heartRateZones[1].min}, title: 'Fat Burn Min' },
            { render: function(data, type, row) {return parseFloat(row.value.heartRateZones[1].caloriesOut.toFixed(2))}, title: 'Fat Burn Calories' },
            { render: function(data, type, row) {return row.value.heartRateZones[1].minutes}, title: 'Fat Burn Minutes' },
            {render: function(data, type, row) {return row.value.heartRateZones[2].max}, title: 'Cardio Max' },
            { render: function(data, type, row) {return row.value.heartRateZones[2].min}, title: 'Cardio Min' },
            {render: function(data, type, row) {return parseFloat(row.value.heartRateZones[2].caloriesOut.toFixed(2))}, title: 'Cardio Calories' },
            { render: function(data, type, row) {return row.value.heartRateZones[2].minutes}, title: 'Cardio Minutes' },
            { render: function(data, type, row) {return row.value.heartRateZones[3].max}, title: 'Peak Max' },
            { render: function(data, type, row) {return row.value.heartRateZones[3].min}, title: 'Peak Min' },
            {render: function(data, type, row) {return parseFloat(row.value.heartRateZones[3].caloriesOut.toFixed(2))}, title: 'Peak Calories' },
            { render: function(data, type, row) {return row.value.heartRateZones[3].minutes}, title: 'Peak Minutes' },
            // { data: 'value.restingHeartRate', title: 'Resting Heart Rate' },


           
            // Add more columns as needed
        ],
        initComplete: function(settings, json) {
            console.log(json);
        }
    });

    table.columns.adjust().draw();
});