function docVersionShow() {
    $('#doc-versions').addClass('doc-versions-active');
    $('#doc-versions-banner').one('click', docVersionHide);
}
function docVersionHide( event ) {
    $('#doc-versions').removeClass('doc-versions-active');
    event.stopPropagation();
    $('#doc-versions').one('click', docVersionShow);
}
$('#doc-versions').one('click', docVersionShow);

$('#doc-versions').mousedown(function(event) {
    if (event.which == 2) {
        $('#doc-versions').css('display', 'none');
    }
});

$('#doc-versions').on('touchstart', function(event) {
    var swipe = event.originalEvent.touches
    original = swipe[0].pageX;

    $(this).on('touchmove', function(event) {
        var contact = event.originalEvent.touches,
        distance = contact[0].pageX - original;

        if (distance > 50) {
            $('#doc-versions').css('display', 'none');
        }
    })
});
