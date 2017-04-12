# SSRF Testing

### htaccess - redirect test for various cases
Status codes: 300, 301, 302, 303, 307, 308
Filetypes: jpg, json, csv, xml
#### Live demo:
jpg 301 response without and with valid response body
https://ssrf.localdomain.pw/img-without-body/301-http-169.254.169.254:80-.i.jpg
https://ssrf.localdomain.pw/img-with-body/301-https-169.254.169.254:80-.i.jpg

json 301 response without and with valid response body
https://ssrf.localdomain.pw/json-without-body/301-http-169.254.169.254:80-.j.json
https://ssrf.localdomain.pw/json-with-body/301-http-169.254.169.254:80-.j.json

csv 301 response without and with valid response body
https://ssrf.localdomain.pw/csv-without-body/301-https-169.254.169.254:80-.c.csv
https://ssrf.localdomain.pw/csv-with-body/301-https-169.254.169.254:80-.c.csv

xml 301 response without and with valid response body
https://ssrf.localdomain.pw/xml-without-body/301-http-169.254.169.254:80-.x.xml
https://ssrf.localdomain.pw/xml-with-body/301-http-169.254.169.254:80-.x.xml

### cloud-metadata.txt - Cloud Metadata Dictionary useful for SSRF Testing



### AppSecEU15-Server_side_browsing_considered_harmful.pdf
https://www.youtube.com/watch?v=8t5-A4ASTIU



### SSRF bible
https://docs.google.com/document/d/1v1TkWZtrhzRLy0bYXBcdLUedXGb9njTNIJXa3u9akHM
