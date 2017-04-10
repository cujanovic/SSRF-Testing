<?php
header("HTTP/1.1 302 Found");
header("Location: ".$_GET["url"]);
header("Content-Type:application/json");
echo '{"test":"test"}';
