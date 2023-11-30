$(document).ready(function() {
    // Get the token from the sessionStorage
    var access_token = sessionStorage.getItem('access_token');
    console.log("access_token",access_token);



    var table = $('#recentFoodTable').DataTable({
        dom: 'Bfrtip',
        buttons: [
            'copy', 'csv', 'excel', 'pdf', 'print'
        ],
        scrollX: true,
        autoWidth: false,
        deferRender: true, // This will defer the rendering until DataTables is ready to do so
        ajax: {
            url: 'http://localhost:8080/api/nutrition/recent_food/' ,
            type: 'GET',
            headers: {
                'Authorization': 'Bearer ' + access_token
            },
            dataSrc: ''

        },
        columns: [

            { data: 'accessLevel', title: 'Access Level' },
            { data: 'amount', title: 'Amount' },
            { data: 'brand', title: 'Brand' },
            { data: 'calories', title: 'Calories' },
            { data: 'locale', title: 'Locale' },
            { data: 'name', title: 'Name' },
            { data: 'unit.name', title: 'Unit' },
            { data: 'dateLastEaten', title: 'Date Last Eaten' },

            // Add more columns as needed
        ],
        initComplete: function(settings, json) {
            console.log(json);
        }
    });

    table.columns.adjust().draw();
});