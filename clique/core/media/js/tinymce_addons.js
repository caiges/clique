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
        if($.url != undefined && $.url != null) {
            if($.url.param('links') != undefined && $.url.param('links') != null) {
                var linkIds = $.url.param('links');
                if(linkIds != 'undefined' && linkIds != null) {
                    linkIds = linkIds.split(',');
        
                    for(var j = 0; j < linkIds.length; j++) {
                        editor.dom.setStyle(linkIds[j], 'border', '2px solid red');
                    }
                }
            }
        }
    };
    
    tinyMCE.onAddEditor.add(function(mgr,ed) {
        // Setup callback for editor init.
        ed.onInit.add(function(ed) { highlightCallback(ed); });
    });
    
});
