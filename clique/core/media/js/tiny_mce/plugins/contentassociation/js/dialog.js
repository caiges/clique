tinyMCEPopup.requireLangPack();

var ContentAssociationDialog = {
    
	init : function() {
		var f = document.forms[0];
        
        var callbacks = {
            
            success : function(data) {
                var content_items = jQuery.parseJSON(data);
                var optionsHTML = new Array();
                for(var i = 0; i < content_items.length; i++ ) {
                    optionsHTML.push('<option value="' + content_items[i].model + '-' + content_items[i].id + '">' + content_items[i].name + '</option>');
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
		var selectedNode = tinyMCEPopup.editor.selection.getNode();
        var selectedContentItem = $('#content-items').val();
        var sourceItem = tinyMCEPopup.getWin().document.getElementById('model_name').value + '-' + tinyMCEPopup.getWin().document.getElementById('model_id').value;
        var data = {item : selectedContentItem, source_item : sourceItem}
		var callbacks = {
            
            success : function(data) {
                var content_association = jQuery.parseJSON(data);
        		tinyMCEPopup.editor.execCommand('mceInsertContent', false, '<a class="' + content_association.target_model_link_class + '" href="' + content_association.target_model_link + '" rel="contentassociation">' + $(selectedNode).html() + '</a>');
        		tinyMCEPopup.close();
            },
            
            error : function(data) {
                alert('Problem with content association.');
            }
        }
         
        $.ajax({url : '/content-association/content_items.json', type : 'POST', data : data, success : callbacks.success, error : callbacks.error});
        
	}
};

tinyMCEPopup.onInit.add(ContentAssociationDialog.init, ContentAssociationDialog);
