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
