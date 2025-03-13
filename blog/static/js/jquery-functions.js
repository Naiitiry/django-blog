
$(document).ready(function () {
    // Si hay mensajes en el modal, abrirlo automáticamente
    if ($("#modal-body .alert").length > 0) {
        $("#messageModal").fadeIn();
    }

    // Cerrar el modal al hacer clic en la "X"
    $(".close").click(function () {
        $("#messageModal").fadeOut();
    });

    // Cerrar el modal si se hace clic fuera de él
    $(window).click(function (e) {
    if ($(e.target).is("#messageModal")) {
        $("#messageModal").fadeOut();
    }
    });
});
$(document).ready(function() {
    $("#toggleMenu").click(function() {
        $("#menu").toggleClass("show");
    });
    // Cerrar el menú si se hace clic fuera
    $(document).click(function(event) {
        if (!$(event.target).closest("#menu, #toggleMenu").length) {
            $("#menu").removeClass("show");
        }
    });
});