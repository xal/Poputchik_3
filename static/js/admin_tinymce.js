function tinyDjangoBrowser(field_name, url, type, win) {
    var managerURL;
    if (type == 'file') {
        managerURL = window.location.toString() + '../../../content/document/';
    } else {
        managerURL = window.location.toString() + '../../../content/flatimage/';
    }
    tinyMCE.activeEditor.windowManager.open({
        file: managerURL,
        title: 'Click to picture',
        width: 800,
        height: 450,
        resizable: 'yes',
        inline: 'yes',
        close_previous: 'no',
        popup_css : false
    }, {
        window: win,
        input: field_name
    });

    return false;
}


$(function() {
    var tinymceOptions = {
        script_url: '/static/tiny_mce/tiny_mce.js',
        content_css : "/static/css/style_mce.css",
        theme: 'advanced',
        plugins: 'safari,pagebreak,advhr,advimage,advlink,inlinepopups,media,searchreplace,contextmenu,fullscreen,noneditable, table',
        theme_advanced_buttons1: 'code,removeformat,bold,italic,underline,strikethrough,|,justifyleft,justifycenter,justifyright,justifyfull,formatselect,fontselect,fontsizeselect',
        theme_advanced_buttons2: 'undo,redo,|search,replace,|,bullist,numlist,|,outdent,indent,blockquote,|,link,unlink,anchor,image,cleanup,|,forecolor,backcolor|,sub,sup',
        theme_advanced_buttons3: 'tablecontrols',
        theme_advanced_buttons4: '',
        theme_advanced_toolbar_location: 'top',
        theme_advanced_toolbar_align: 'left',
        theme_advanced_statusbar_location: 'bottom',
        relative_urls: false,
        // theme_advanced_resizing: true,
        width: 800,
        height: 600,
        force_br_newlines : true,
        force_p_newlines : false,
        forced_root_block : '', 
        // Drop lists for link/image/media/template dialogs
        template_external_list_url: 'lists/template_list.js',
        external_link_list_url: 'lists/link_list.js',
        external_image_list_url: 'lists/image_list.js',
        media_external_list_url: 'lists/media_list.js',
        extended_valid_elements : 'span[class|style],code[class],iframe[src|width|height|name|align|frameborder|scrolling]',

        doctype: '<!DOCTYPE html>',
        file_browser_callback: 'tinyDjangoBrowser'
    };

    $('textarea:not(.plain)').tinymce(tinymceOptions);
});

