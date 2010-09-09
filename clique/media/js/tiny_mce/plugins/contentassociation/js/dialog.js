tinyMCEPopup.requireLangPack();

var ContentAssociationDialog = {
	init : function() {
		var f = document.forms[0];
        
        var callbacks = {
            
            success : function(data) {
                var productsJSON = jQuery.parseJSON(data);
                var optionsHTML = new Array();
                for(var i = 0; i < productsJSON.length; i++ ) {
                    optionsHTML.push('<option value="' + productsJSON[i].pk + '">' + productsJSON[i].fields.name + '</option>');
                }            
                $('#products').html(optionsHTML.join(''));
            },
            
            error : function(data) {
                
            }
        }
            
        $.ajax({url : '/product-association/products.json', success : callbacks.success, error : callbacks.error});
        
		// Get the selected contents as text and place it in the input
		f.products.value = tinyMCEPopup.editor.selection.getContent({format : 'text'});
		//f.somearg.value = tinyMCEPopup.getWindowArg('some_custom_arg');
	},

	insert : function() {
		// Insert the contents from the input into the document
		var selectedText = tinyMCEPopup.editor.selection.getContent({format : 'text'});
		//document.forms[0].products.value
		tinyMCEPopup.editor.execCommand('mceInsertContent', false, '<a href="#">' + selectedText + '</a>');
		tinyMCEPopup.close();
	}
};

tinyMCEPopup.onInit.add(ContentAssociationDialog.init, ContentAssociationDialog);
