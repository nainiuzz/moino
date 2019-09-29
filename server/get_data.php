<?php

$type = $_GET["data"];
$file_text = "failed";

switch($type){
    case "function":
        $file_text = htmlentities(file_get_contents("function.dat"));
        echo base64_decode($file_text);
    break;
    
    case "station":
        $file_text = htmlentities(file_get_contents("station.dat"));
        echo base64_decode($file_text);
    break;
}
?>