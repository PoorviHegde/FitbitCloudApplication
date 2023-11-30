$(document).ready(function() {
    // Get the token from the sessionStorage
    var access_token = sessionStorage.getItem('access_token');
    console.log("access_token",access_token);


    var table = $('#devicesTable').DataTable({
        dom: 'Bfrtip',
        buttons: [
            'copy', 'csv', 'excel', 'pdf', 'print'
        ],
        scrollX: true,
        autoWidth: false,
        deferRender: true, // This will defer the rendering until DataTables is ready to do so
        ajax: {
            url: 'http://localhost:8080/api/devices' ,
            type: 'GET',
            headers: {
                'Authorization': 'Bearer ' + access_token
            },
            dataSrc: ''

        },
        columns: [

            { data: 'battery', title: 'Battery' },
            { data: 'batteryLevel', title: 'Battery Level' },
            { data: 'deviceVersion', title: 'Device Version' },
            { data: 'id', title: 'Id' },
            { data: 'lastSyncTime', title: 'Last Sync Time' },
            { data: 'mac', title: 'Mac' },
            { data: 'type', title: 'Type' },
           
            // Add more columns as needed
        ],
        initComplete: function(settings, json) {
            console.log(json);
        }
    });

    table.columns.adjust().draw();
});