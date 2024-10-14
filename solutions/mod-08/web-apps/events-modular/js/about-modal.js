// about-modal.js
$(document).ready(function() {
    $('#navbar-placeholder').load('navbar.html', function() {
        $('#aboutMenuItem').on('click', function() {
            var aboutModal = new bootstrap.Modal(document.getElementById('aboutModal'));
            aboutModal.show();
        });
    });

    $('#about-modal-placeholder').load('modals/about-modal.html');
});
