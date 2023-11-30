$(document).ready(function() {
    // Get the token from the sessionStorage
    var access_token = sessionStorage.getItem('access_token');
    console.log("access_token",access_token);

    var urlParams = new URLSearchParams(window.location.search);
    var date = urlParams.get('date');

    console.log('Date:', date);

        // Validate and encode the date
    var datePattern = /^\d{4}-\d{2}-\d{2}$/; // YYYY-MM-DD
    if (!datePattern.test(date) ) {
        console.error('Invalid date format');
        return;
    }
    var encodedDateStart = encodeURIComponent(date);
   


    var table = $('#foodTable').DataTable({
        dom: 'Bfrtip',
        buttons: [
            'copy', 'csv', 'excel', 'pdf', 'print'
        ],
        scrollX: true,
        autoWidth: false,
        deferRender: true, // This will defer the rendering until DataTables is ready to do so
        ajax: {
            url: 'http://localhost:8080/api/nutrition/food_log/' + encodedDateStart + '/',
            type: 'GET',
            headers: {
                'Authorization': 'Bearer ' + access_token
            },
            dataSrc: 'foods'

        },
        columns: [

            { data: 'isFavorite', title: 'Is Favorite?' },
            { data: 'date', title: 'Date' },
            { data: 'loggedFood.accessLevel', title: 'Access Level' },
            { data: 'loggedFood.amount', title: 'Amount' },
            { data: 'loggedFood.brand', title: 'Brand' },
            { data: 'loggedFood.calories', title: 'Calories' },
            { data: 'loggedFood.locale', title: 'Locale' },
            { data: 'loggedFood.name', title: 'Name' },
            { data: 'loggedFood.unit.name', title: 'Unit' },

        

           
            // Add more columns as needed
        ],
        initComplete: function(settings, json) {
            console.log(json);
        }
    });

    table.columns.adjust().draw();
});