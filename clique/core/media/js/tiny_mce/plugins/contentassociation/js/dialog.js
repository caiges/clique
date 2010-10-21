tinyMCEPopup.requireLangPack();

var ContentAssociationDialog = {
    
	init : function() {
		var f = document.forms[0];
        
        var callbacks = {
            
            success : function(data) {
                var content_items = jQuery.parseJSON(data);
                var optionsHTML = new Array();
                for(var i = 0; i < content_items.length; i++ ) {
                    optionsHTML.push('<option value="' + content_items[i].pk + '">' + content_items[i].fields.name + '</option>');
                }            
                $('#content-items').html(optionsHTML.join(''));
            },
            
            error : function(data) {
                
            }
        }
            
        $.ajax({url : '/content-association/content_items.json', success : callbacks.success, error : callbacks.error});
        
		// Get the selected contents as text and place it in the input
		//$('#content-items').val() = tinyMCEPopup.editor.selection.getContent({format : 'text'});
		//f.somearg.value = tinyMCEPopup.getWindowArg('some_custom_arg');
	},

	insert : function() {
		// Insert the contents from the input into the document
		var selectedText = tinyMCEPopup.editor.selection.getContent({format : 'text'});
		//document.forms[0].products.value
		var callbacks = {
            
            success : function(data) {
                var content_association = jQuery.parseJSON(data);
                
        		tinyMCEPopup.editor.execCommand('mceInsertContent', false, '<a href="#">' + selectedText + '</a>');
        		tinyMCEPopup.close();
            },
            
            error : function(data) {
                alert('Problem with content association.');
            }
        }
         
        $.ajax({url : '/content-association/content_items.json', type : 'POST', success : callbacks.success, error : callbacks.error});
        
	}
};

tinyMCEPopup.onInit.add(ContentAssociationDialog.init, ContentAssociationDialog);
