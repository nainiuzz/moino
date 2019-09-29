<?php
$namefunction = $_GET["function"];
$namestation = $_GET["station"];
$password = $_GET["password"];

if(sha1($password) == "sha1_pass"){
    $result = true;
    
    if($namefunction != ""){
        $fp = fopen("function.dat", "w+");
        fwrite($fp, base64_encode($namefunction));
        fclose($fp);
        
    }else $result = false;
    
    if($namestation == "connected" or $namestation == "disconnected"){
        $fp = fopen("station.dat", "w+");
        fwrite($fp, base64_encode($namestation));
        fclose($fp);
        $result = true;
        
    }else $result = false;
    
    if($result){
        echo "successfully";
        
    }else echo "failed";
}else echo "failed";
?>