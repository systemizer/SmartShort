$(document).ready(function(){
    var shared;
    var scrolled;
    
    //console.log("sending get_highlighted request");
    
    
    chrome.tabs.getSelected(null, function(tab) {
      chrome.tabs.sendRequest(tab.id, {'type' : 'get_highlighted'}, function(response) {
          shared = response.shared;
          if(shared === undefined) return;          
	  //console.log('asking for url from server');
          $.ajax({'dataType':'jsonp','url':'http://leapto.it/extension/create/?callback=func', 'data':{'url' : tab.url, 'shared' : shared, 'scrolled' : 0}, 'success':function(response){$("#result_container").html("Share This Link! " + response.url);
          }});
        });
    });
});


