import http.client
conn = http.client.HTTPConnection("10,xx,x,xx")

//Data post

payload = "[\n {\n \"ServerIp\": \"10.10.0.38\",\n" \
          "\"TargetType\": \"Linux\",\n \"UserName\": " \
          "\"vasant2701\",\n\"DbInstanceName\": \"\",\n " \
          "\"OpenForHours\": \"1\"\n },\n{\n \"ServerIp\": " \
          "\"10.10.0.204\",\n \"TargetType\":\"Linux\",\n \"UserName\": " \
          "\"user22\",\n \"DbInstanceName\":\"\",\n \"OpenForHours\": \"1\"\n }\n]"
headers = {'Authorization': "bearer eyJ0eXAiOiJKV1[... Removed for brevity ....]WR097oFM",
           'Content-Type': "application/json",
           'User-Agent': "PostmanRuntime/7.18.0",
           'Accept': "*/*",'Cache-Control': "no-cache",
           'Postman-Token': "c12a0630-619a-4b5c-a720-ffc05f51f179,a9a3dd04-5bcf-45f3-8bdc-aeb701c1c3c9",
           'Host': "10.xx.x.xx:4xx2",
           'Accept-Encoding': "gzip, deflate",
           'Content-Length': "339",
           'Cookie': "ASP.NET_SessionId=euh4j3ypscazrj33u1iohh2x",
           'Connection': "keep-alive",
           'cache-control': "no-cache"}

conn.request("POST", "api,ServicePassword,GetTargetDevicePassKey", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))