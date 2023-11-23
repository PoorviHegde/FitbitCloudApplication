$(document).ready(function() {
    // Get the token from the sessionStorage
    var access_token = sessionStorage.getItem('access_token');
    console.log("access_token",access_token);

    var urlParams = new URLSearchParams(window.location.search);


    var table = $('#friendsTable').DataTable({
        scrollX: true,
        autoWidth: false,
        deferRender: true, // This will defer the rendering until DataTables is ready to do so
        ajax: {
            url: 'http://localhost:8080/api/friends' ,
            type: 'GET',
            headers: {
                'Authorization': 'Bearer ' + access_token
            },
            dataSrc: ''

        },
        columns: [

            { data: 'type', title: 'Type' },
            { data: 'id', title: 'ID' },
            { data: 'attributes.avatar', title: 'Avatar' },
            { data: 'attributes.child', title: 'Child' },
            { data: 'attributes.friend', title: 'Friend' },
            { data: 'attributes.name', title: 'Name' }

           
            // Add more columns as needed
        ],
        initComplete: function(settings, json) {
            console.log(json);
        }
    });

    table.columns.adjust().draw();
});