$(document).ready(function() {        
        
    var highlightCallback = function(editor) {

        // Highlight each conflicting form field.
        if(typeof $.url != undefined && $.url != null) {
            if(typeof $.url.param('field_ids') != undefined && $.url.param('field_ids') != null) {
                var $fields = $.url.param('field_ids').split(',');

                for(var i = 0; i < $fields.length; i++) {
                    if(tinyMCE.editors[$fields[i]].id == editor.id) {
                        $('#' + $fields[i] + '_tbl').css('border', '2px solid red');
                    }
                }
            }
        }
        
        // Highlight each conflicting link.
        if(typeof $.url != undefined && $.url != null) {
            if(typeof $.url.param('links') != undefined && $.url.param('links') != null) {
                var linkIds = $.url.param('links');
                if(linkIds != 'undefined' && linkIds != null) {
                    linkIds = linkIds.split(',');
        
                    for(var j = 0; j < linkIds.length; j++) {
                        editor.dom.addClass(linkIds[j], 'contentassociationconflict');
                    }
                }
            }
        }
        
        // Highlight content associations that are no longer valid.
        var invalid_content_associations_url = '/content-association/content_items/invalid.json';
        var $model_name = $('#model_name');
        var $model_id = $('#model_id');
        
        var callbacks = {
            
            success : function(data) {
                var linkIds = $.parseJSON(data);
                //console.log(linkIds);
                for(var j = 0; j < linkIds.length; j++) { 
                    editor.dom.addClass(linkIds[j], 'contentassociationconflict');
                }             
            },
            
            error : function(data) {
                // Do nothing.
            }
        };
        
        //$.ajax({url : invalid_content_associations_url, type : 'POST', data : {model_name : $model_name.val(), model_id : $model_id.val()}, success : callbacks.success, error : callbacks.error});
    
        
        
    };
    
    tinyMCE.onAddEditor.add(function(mgr,ed) {
        // Setup callback for editor init.
        ed.onInit.add(function(ed) { highlightCallback(ed); });
    });
    
});
