import urllib,urllib2


def test_create_url():
    create_url = "%s/extension/create/" % settings.DOMAIN

    #Test that a get request will response with a 404
    req = urllib2.Request(url)
    response = urllib2.open(req)
    assert response.code==404


    # Test successful submission of data
    data = {'url':'http://google.com',
            'shared':'This is the text that was shared',
            'scrolled':10}
    req = urllib2.Request(url,data)
    rep = urllib2.open(req)
    assert rep.code==200
    
    response_data = json.loads(rep.read())
    assert response_data.has_attr("url")

    
