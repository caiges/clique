(function(){tinymce.PluginManager.requireLangPack('contentassociation');tinymce.create('tinymce.plugins.ContentAssociation',{init:function(ed,url){ed.addCommand('mceContentAssociation',function(){ed.windowManager.open({file:url+'/dialog.htm',width:320+parseInt(ed.getLang('contentassociation.delta_width',0)),height:120+parseInt(ed.getLang('contentassociation.delta_height',0)),inline:1},{plugin_url:url,some_custom_arg:'custom arg'})});ed.addButton('contentassociation',{title:'contentassociation.desc',cmd:'mceContentAssociation',image:url+'/img/example.gif'});ed.onNodeChange.add(function(ed,cm,n){cm.setActive('contentassociation',n.nodeName=='IMG')})},createControl:function(n,cm){return null},getInfo:function(){return{longname:'Content Association plugin',author:'Caige Nichols',authorurl:'http://www.zionandzion.com/',infourl:'http://wiki.moxiecode.com/index.php/TinyMCE:Plugins/example',version:"1.0"}}});tinymce.PluginManager.add('contentassociation',tinymce.plugins.ContentAssociationPlugin)})();