var ourTabs = {};
var id;

chrome.extension.onRequest.addListener(
  function(request, sender, sendResponse) {
    if(request.type == "ourSite"){
        //console.log(sender.tab.url);
	//console.log("our site");
        id = sender.tab.url.split("=")[1];
        //console.log(id);
        var urlReceived;
        var textReceived;
        //console.log("bg asking server for new url");
        $.ajax({'dataType':'jsonp','url':'http://semlinked.com:8989/extension/get/?callback=func&id=' + id, 'success':function(response){ 
            response= eval(response);
            //console.log("respo: " + response);
            urlReceived = response.url;
            textReceived = response.shared;
            ourTabs[sender.tab.id] = {'tab': sender.tab, 'data' : {'url': urlReceived, 'shared' : textReceived, 'scrolled' : 0}};
            //console.log("url: " + urlReceived);
            sendResponse({'message': 'added the tab!', 'url': urlReceived});
        }});
    }
    else{
        //console.log("our tab ids: ") 
        //for(var i in ourTabs) console.log(i);
        //console.log("this tab: " + sender.tab.id);
	//console.log("external site");
        if(sender.tab.id in ourTabs){
	//console.log("in tabs");
          //console.log('the tab is in our tabs. ');
          // redirection done already. so we delete it.
          sendResponse({'data' : ourTabs[sender.tab.id]['data']});
          //console.log(ourTabs[sender.tab.id].data);
          delete ourTabs[sender.tab.id];
        }else{
            sendResponse({});
        }
    }
  }
);
