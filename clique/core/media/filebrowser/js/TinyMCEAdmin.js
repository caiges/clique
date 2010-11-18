function CustomFileBrowser(field_name, url, type, win) {

    var cmsURL = "/admin/filebrowser/browse/?pop=2";
    cmsURL = cmsURL + "&type=" + type;
    
    tinyMCE.activeEditor.windowManager.open({
        file: cmsURL,
        width: 820,  // Your dimensions may differ - toy around with them!
        height: 500,
        resizable: "yes",
        scrollbars: "yes",
        inline: "no",  // This parameter only has an effect if you use the inlinepopups plugin!
        close_previous: "no"
    }, {
        window: win,
        input: field_name,
        editor_id: tinyMCE.selectedInstance.editorId
    });
    return false;
}


tinyMCE.init({
    mode: "textareas",
    theme: "advanced",
    language: "en",
    skin: "o2k7",
    browsers: "gecko",
    dialog_type: "modal",
    object_resizing: true,
    cleanup_on_startup: true,
    forced_root_block: "p",
    remove_trailing_nbsp: true,
    theme_advanced_toolbar_location: "top",
    theme_advanced_toolbar_align: "left",
    theme_advanced_statusbar_location: "none",
    theme_advanced_buttons1: "formatselect,bold,italic,underline,bullist,numlist,|,justifyleft,justifycenter,justifyright,justifyfull,|,undo,redo,anchor,link,unlink,hr,template,image,code,removeformat,fullscreen,cut,copy,paste,pastetext,pasteword,media,charmap,contentassociationlink,contentassociationunlink,|,tablecontrols",
    theme_advanced_buttons2: "",
    theme_advanced_buttons3: "",
    theme_advanced_path: false,
    theme_advanced_blockformats: "p,h1,h2,h3,h4,h5,h6",
    plugins: "safari,pagebreak,style,layer,table,save,advhr,advimage,advlink,emotions,iespell,insertdatetime,preview,media,searchreplace,print,contextmenu,paste,directionality,fullscreen,noneditable,visualchars,nonbreaking,xhtmlxtras,template,contentassociation",
    advimage_styles: "Linksbündig neben Text=img_left;Rechtsbündig neben Text=img_right;Eigener Block=img_block",
    advlink_styles: "internal (sehmaschine.net)=internal;external (link to an external site)=external",
    advimage_update_dimensions_onchange: true,
    file_browser_callback: "CustomFileBrowser",
    relative_urls: false,
    convert_urls : false,
    theme_advanced_resizing : true,
	template_templates : [
	    {
	        title : "Standard Recipe",
	        src : "/media/js/tiny_mce/templates/recipe.html",
	        description : "Standard recipe template."
        },
        {
	        title : "Standard Page",
	        src : "/media/js/tiny_mce/templates/page.html",
	        description : "Standard page template."
        },
        {
	        title : "Standard Product",
	        src : "/media/js/tiny_mce/templates/product.html",
	        description : "Standard product template."
        }
    ],
    width: '90%',
    height: '500px'
});


