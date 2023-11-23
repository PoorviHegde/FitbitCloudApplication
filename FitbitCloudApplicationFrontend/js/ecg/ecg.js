$(document).ready(function() {
    // Get the token from the sessionStorage
    var access_token = sessionStorage.getItem('access_token');
    console.log("access_token",access_token);

    var urlParams = new URLSearchParams(window.location.search);


    var table = $('#ecgTable').DataTable({
        scrollX: true,
        autoWidth: false,
        deferRender: true, // This will defer the rendering until DataTables is ready to do so
        ajax: {
            url: 'http://localhost:8080/api/ecg' ,
            type: 'GET',
            headers: {
                'Authorization': 'Bearer ' + access_token
            },
            dataSrc: 'ecgReadings'

        },
        columns: [

            { data: 'averageHeartRate', title: 'Average Heart Rate' },
            { data: 'deviceName', title: 'Device Name' },
            { data: 'featureVersion', title: 'Feature Version' },
            { data: 'firmwareVersion', title: 'Firmware Version' },
            { data: 'leadNumber', title: 'Lead Number' },
            { data: 'numberOfWaveformSamples', title: 'Number of wave from Samples' },
            { data: 'resultClassification', title: 'Result Classification' },
            { data: 'samplingFrequencyHz', title: 'Sampling Frequency in Hertz' },
            { data: 'scalingFactor', title: 'Scaling Factor' },
            { data: 'startTime', title: 'Start Time' },
           
            // Add more columns as needed
        ],
        initComplete: function(settings, json) {
            console.log(json);
        }
    });

    table.columns.adjust().draw();
});