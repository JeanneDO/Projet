<?php
 
$param1 = $_POST['team1'];
$param2 = $_POST['team2'];
 
$command = "python interface.py";

header('Content-Type: text/html; charset=utf-8');
echo '<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />';
echo "<style type='text/css'>
 body{
 //background:#000;
 color: rgba(0,0,255,0.55);
 font-family: Georgia, serif;
 font-size: 200%;
 font-weight: 600;
 }
 </style>";

$pid = popen( $command,"r");
 
echo "<body><pre>";
while( !feof( $pid ) )
{
 echo fread($pid, 256);
 flush();
 ob_flush();
 echo "<script>window.scrollTo(0,99999);</script>";
 usleep(100000);
}
pclose($pid);
 
echo "</pre><script>window.scrollTo(0,99999);</script>";

?>
