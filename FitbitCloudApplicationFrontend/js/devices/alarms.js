$(document).ready(function() {
    // Get the token from the sessionStorage
    var access_token = sessionStorage.getItem('access_token');
    console.log("access_token",access_token);

    var urlParams = new URLSearchParams(window.location.search);



    var table = $('#alarmsTable').DataTable({
        dom: 'Bfrtip',
        buttons: [
            'copy', 'csv', 'excel', 'pdf', 'print'
        ],
        scrollX: true,
        autoWidth: false,
        deferRender: true, // This will defer the rendering until DataTables is ready to do so
        ajax: {
            url: 'http://localhost:8080/api/tracker/2470017778' ,
            type: 'GET',
            headers: {
                'Authorization': 'Bearer ' + access_token
            },
            dataSrc: 'alarms'

        },
        columns: [

            { data: 'dateTime', title: 'Date Time' },
            { data: 'value.vo2Max', title: 'Cardio Score' }
           
            // Add more columns as needed
        ],
        initComplete: function(settings, json) {
            console.log(json);
        }
    });

    table.columns.adjust().draw();
});