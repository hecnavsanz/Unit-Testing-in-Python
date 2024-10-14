// events-list.js
document.addEventListener('DOMContentLoaded', function() {
    var eventData = JSON.parse(sessionStorage.getItem('eventData')) || [];
    var tableBody = document.getElementById('eventsTableBody');
    var deleteIndex = null;

    // Load the delete confirmation modal
    $('#delete-confirm-modal-placeholder').load('modals/delete-confirm-modal.html', function() {
        // Add event listener for the confirm delete button after the modal is loaded
        document.getElementById('confirmDeleteBtn').addEventListener('click', function() {
            if (deleteIndex !== null) {
                eventData.splice(deleteIndex, 1);
                sessionStorage.setItem('eventData', JSON.stringify(eventData));
                tableBody.children[deleteIndex].remove();
                deleteIndex = null;
                var deleteConfirmModal = bootstrap.Modal.getInstance(document.getElementById('deleteConfirmModal'));
                deleteConfirmModal.hide();
            }
        });
    });

    // Populate the table with event data
    eventData.forEach(function(event, index) {
        var row = document.createElement('tr');
        row.innerHTML = `
            <td>${event['ce-description']}</td>
            <td>${event['ce-active-check'] ? 'Yes' : 'No'}</td>
            <td>${event['ce-scope-radio']}</td>
            <td>${event['ce-date'] ? event['ce-date'] : ''}</td>
            <td><button class="btn btn-danger btn-sm delete-btn" data-index="${index}">Delete</button></td>
        `;
        tableBody.appendChild(row);
    });

    // Event delegation for delete buttons
    tableBody.addEventListener('click', function(event) {
        if (event.target.classList.contains('delete-btn')) {
            deleteIndex = event.target.getAttribute('data-index');
            var deleteConfirmModal = new bootstrap.Modal(document.getElementById('deleteConfirmModal'));
            deleteConfirmModal.show();
        }
    });
});
