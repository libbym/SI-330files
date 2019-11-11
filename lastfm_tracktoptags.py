import urllib.request, json 
with urllib.request.urlopen("http://ws.audioscrobbler.com/2.0/?method=track.gettoptags&artist=radiohead&track=paranoid+android&api_key=c481aa7d12779c7c952708e61f4ff05f&format=json") as url1:
    data1 = json.loads(url1.read().decode())
    print(data1)