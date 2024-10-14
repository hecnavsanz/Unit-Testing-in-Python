// event-create.js
$(document).ready(function() {
    $('[name="ce-date"]').datepicker({
        format: 'mm/dd/yyyy',
        autoclose: true,
        todayHighlight: true
    });

    $('#event-form').on('submit', function(event) {
        event.preventDefault();
        // Create JSON object from form data
        var jsonData = {};
        jsonData['ce-description'] = $('[name="ce-description"]').val();
        jsonData['ce-active-check'] = $('#ce-active-check').is(':checked');
        jsonData['ce-scope-radio'] = $('input[name="ce-scope-radio"]:checked').attr('id');
        jsonData['ce-date'] = $('[name="ce-date"]').datepicker('getDate');
        // Validate that the event date is not null
        if (!jsonData['ce-date']) {
            alert('Event Date cannot be empty.');
            return;
        }
        // Retrieve existing eventData from sessionStorage or initialize as an empty array
        var eventData = JSON.parse(sessionStorage.getItem('eventData')) || [];
        if (!Array.isArray(eventData)) {
            eventData = [];
        }
        // Add new event to the array
        eventData.push(jsonData);
        // Store updated eventData back in sessionStorage
        sessionStorage.setItem('eventData', JSON.stringify(eventData));
        $('#eventData').text(JSON.stringify(jsonData, null, 2));
        $('#eventModal').modal('show');
        this.reset();
    });

    // Load the JSON Data Modal
    $('#json-data-modal-placeholder').load('modals/display-json-data-modal.html');
});
