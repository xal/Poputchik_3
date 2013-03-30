$(function() {
    if (window.parent) {
        $('#changelist tbody a.image-picker').click(function(e) {
            var url = $(this).attr('href');
            var win = tinyMCEPopup.getWindowArg("window");
            var alt = $(this).find('img').attr('alt');

            win.document.getElementById(tinyMCEPopup.getWindowArg("input")).value = url;
            win.document.getElementById('alt').value = alt;

            if (typeof(win.ImageDialog) != "undefined") {
                if (win.ImageDialog.getImageData) win.ImageDialog.getImageData();
                if (win.ImageDialog.showPreviewImage) win.ImageDialog.showPreviewImage(url);
            }

            tinyMCEPopup.close();
            return false;
        });
        $('#changelist tbody a.file-picker').click(function(e) {
            var url = $(this).attr('href');
            var win = tinyMCEPopup.getWindowArg("window");
            win.document.getElementById(tinyMCEPopup.getWindowArg("input")).value = url;
            tinyMCEPopup.close();
            return false;
        });
    }
});

