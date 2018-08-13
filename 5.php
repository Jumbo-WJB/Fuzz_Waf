<html>
<body>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>POST注入转表单提交数据小脚本</title>
<form action="sql.php" method="post"
enctype="multipart/form-data">
<label for="sql">Fuck:</label>
<input type="text" name="url"/>
</br>
<label for="parm">POST数据:</label>
<input type="text" name="parm"/>
</br>
<input type="submit" name="submit" value="千年杀" />
</form>
<?php
    $id=@$_POST['url'];$parm=@$_POST['parm'];
    $arr=explode("=",$parm);
    $arr2=explode("&",$parm);
    $num=count($arr2);
    if($num>1){
$arr01=explode("=",$arr2[0]);
for($number=0;$number<$num;$number++){
    $n[$number]=explode("=",$arr2[$number]);
}
    }
?>
<form action=<?php echo $id;?> method="post"
enctype="multipart/form-data">
<input type="text" name=<?php echo $arr[0];?> value=<?php echo $arr[1];?> /></br>
<label for="parm">单参数请点击:</label>
<input type="submit" name="submit" value="submit" />
</form>
</br></br>
<form action=<?php echo $id;?> method="post"
enctype="multipart/form-data">
<input type="text" name=<?php echo @$n[0][0];?> value=<?php echo @$n[0][1];?> /></br>
<input type="text" name=<?php echo @$n[1][0];?> value=<?php echo @$n[1][1];?> /></br>
<input type="text" name=<?php echo @$n[2][0];?> value=<?php echo @$n[2][1];?> /></br>
<input type="text" name=<?php echo @$n[3][0];?> value=<?php echo @$n[3][1];?> /></br>
<input type="text" name=<?php echo @$n[4][0];?> value=<?php echo @$n[4][1];?> /></br>
<input type="text" name=<?php echo @$n[5][0];?> value=<?php echo @$n[5][1];?> /></br>
<input type="text" name=<?php echo @$n[6][0];?> value=<?php echo @$n[6][1];?> /></br>
<input type="text" name=<?php echo @$n[7][0];?> value=<?php echo @$n[7][1];?> /></br>
<input type="text" name=<?php echo @$n[8][0];?> value=<?php echo @$n[8][1];?> /></br>
<input type="text" name=<?php echo @$n[9][0];?> value=<?php echo @$n[9][1];?> /></br>
<label for="parm">多参数请点击:</label>
<input type="submit" name="submit" value="submit" />
</br>
</form>
</body>
</html>
