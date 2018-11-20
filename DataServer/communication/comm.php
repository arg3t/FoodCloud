<?php
/**
 * Created by PhpStorm.
 * User: yigido
 * Date: 6/23/18
 * Time: 5:19 PM
 */


$id = $_POST["id"];
$value = $_POST["value"];
$content = $_POST["content"];
$file_loc =  "../content/" .  $value . "/" . $id . ".json";
$myfile = fopen($file_loc, "r") or die("Unable to open file!");
$send = fread($myfile,filesize($file_loc));
if(isset($_POST["content"])){
    $send = json_decode($send,true);
    $send = $send[$content];
}
echo $send;

?>





