console.log('running external script');


var curelem = document.body;
var result = [];
var loaded = false;

var search = function(cur,target)
{
	//console.log(cur);
	if (!cur) {
		return;
	}
	if (cur.nodeType==3 && cur.hasOwnProperty("textContent") && cur.textContent.indexOf(target)!=-1) {
			result.push(cur.parentElement);
	} else if (cur.hasOwnProperty("innerHTML") && cur.innerHTML.indexOf(target)!=-1) {
		for (var i=0;i<=cur.childNodes.length;i++) {
			search(cur.childNodes[i], target);
		}
	}
}


chrome.extension.sendRequest({'type' : 'externalSiteStart'}, function(response) {
	//console.log('received data: ');
	//console.log(response); 
	if(response.data !== undefined){
	  	//console.log('searching for ' + response.data.shared);
		console.log(response.data.shared);
  		search(document.body, response.data.shared);
  		console.log(result);
		if(result.length !== 0){
			console.log('highlighting');
			$(result[0]).highlight(response.data.shared);
			result[0].scrollIntoView();
		}	
	}
});





chrome.extension.onRequest.addListener(
    function(request, sender, sendResponse) {
        //console.log('got a message');
        if(request.type == "highlight"){
            //console.log(request + " from background");
            highlight(request.data);
            sendResponse({"message" : "highlight done"});
        }else if(request.type == "get_highlighted"){
            //console.log('received get_highlighted request');
            var selection = window.getSelection();           
            sendResponse({"shared" : selection.toString()});
        }
    }
);


function getScrollHeight(){
    return 100;
}

function highlight(data){
	//console.log('highlighting');
	search(document.body, data.shared)[0];
}


