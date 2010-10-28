/**
 * editor_plugin_src.js
 *
 * Copyright 2009, Moxiecode Systems AB
 * Released under LGPL License.
 *
 * License: http://tinymce.moxiecode.com/license
 * Contributing: http://tinymce.moxiecode.com/contributing
 */

(function() {
	// Load plugin specific language pack
	tinymce.PluginManager.requireLangPack('contentassociation');

	tinymce.create('tinymce.plugins.ContentAssociation', {
		/**
		 * Initializes the plugin, this will be executed after the plugin has been created.
		 * This call is done before the editor instance has finished it's initialization so use the onInit event
		 * of the editor instance to intercept that event.
		 *
		 * @param {tinymce.Editor} ed Editor instance that the plugin is initialized in.
		 * @param {string} url Absolute URL to where the plugin is located.
		 */
		init : function(ed, url) {
			// Register the command so that it can be invoked by using tinyMCE.activeEditor.execCommand('mceExample');
			ed.addCommand('mceContentAssociationLinkContent', function() {
				ed.windowManager.open({
					file : url + '/dialog.htm',
					width : 390 + parseInt(ed.getLang('contentassociation.delta_width', 0)),
					height : 210 + parseInt(ed.getLang('contentassociation.delta_height', 0)),
					inline : 1
				}, {
					plugin_url : url, // Plugin absolute URL
				});
			});

            // Register the command so that it can be invoked by using tinyMCE.activeEditor.execCommand('mceExample');
			ed.addCommand('mceContentAssociationUnlinkContent', function() {
			    var se = ed.selection;
                var selectedNode = se.getNode();
                
				// No selection and not in link
				if (se.isCollapsed() && !ed.dom.getParent(selectedNode, 'A'))
					return;
					
				var data = {link_name : $(selectedNode).attr('name')}
		        var callbacks = {
                    
                    success : function(data) {
                        //ed.getDoc().execCommand("unlink", false, null);
                        // Remove link, preserve inner content.
                		var content = $(selectedNode).html();
                		alert(content);
                		ed.dom.setOuterHTML(selectedNode, content);
           
                    },
                    
                    error : function(data) {
                        alert('Problem with content association.');
                    }
                }
                 
                $.ajax({url : '/content-association/content_items/remove.json', type : 'POST', data : data, success : callbacks.success, error : callbacks.error});
			});

			// Register link content button
			ed.addButton('contentassociationlink', {
				title : 'contentassociation.link',
				cmd : 'mceContentAssociationLinkContent',
				image : url + '/img/link-content.png'
			});
            
            // Register link content button
			ed.addButton('contentassociationunlink', {
				title : 'contentassociation.unlink',
				cmd : 'mceContentAssociationUnlinkContent',
				image : url + '/img/unlink-content.png'
			});
			
            // Add a node change handler, selects the button in the UI when a image is selected
			ed.onNodeChange.add(function(ed, cm, n, co) {
			
                cm.setDisabled('contentassociationlink', co && n.nodeName != 'A' && $(n).attr('rel') != 'undefined');
				cm.setActive('contentassociationlink', n.nodeName == 'A' && !n.name && $(n).attr('rel') == 'contentassociation');
				
				cm.setDisabled('contentassociationunlink', co && n.nodeName != 'A');
				cm.setActive('contentassociationunlink', n.nodeName == 'A' && !n.name && $(n).attr('rel') == 'contentassociation');
				
			});
		},

		/**
		 * Creates control instances based in the incomming name. This method is normally not
		 * needed since the addButton method of the tinymce.Editor class is a more easy way of adding buttons
		 * but you sometimes need to create more complex controls like listboxes, split buttons etc then this
		 * method can be used to create those.
		 *
		 * @param {String} n Name of the control to create.
		 * @param {tinymce.ControlManager} cm Control manager to use inorder to create new control.
		 * @return {tinymce.ui.Control} New control instance or null if no control was created.
		 */
		createControl : function(n, cm) {
			return null;
		},

		/**
		 * Returns information about the plugin as a name/value array.
		 * The current keys are longname, author, authorurl, infourl and version.
		 *
		 * @return {Object} Name/value array containing information about the plugin.
		 */
		getInfo : function() {
			return {
				longname : 'Content Association plugin',
				author : 'Caige Nichols',
				authorurl : 'http://www.zionandzion.com/',
				infourl : 'http://wiki.moxiecode.com/index.php/TinyMCE:Plugins/example',
				version : "1.0"
			};
		}
	});

	// Register plugin
	tinymce.PluginManager.add('contentassociation', tinymce.plugins.ContentAssociation);
})();
