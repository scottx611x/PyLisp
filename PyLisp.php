<head>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>

<link href='http://fonts.googleapis.com/css?family=Raleway' rel='stylesheet' type='text/css'>
<link href='animate.css' rel='stylesheet' type='text/css'>
</head>
<script>
$( document ).ready(function() {


function resizeInput() {
    $(this).attr('size', $(this).val().length);
}

$('input[type="text"]')
    // event handler
    .keyup(resizeInput)
    // resize on page load
    .each(resizeInput);
});
</script>

<style>
html{
	background: #004F2D;
	font-family:Raleway;
}
#Exp{
	text-align: center;
	min-width:275px;
	height:65px;
	border-radius:10px;
	border: 2px solid #11445E;
}
#info{
	text-align: center;
	color:white;
}
#info2{
	text-align: center;
	color:white;
}
input{

 display: block;
 margin: 20px;
 padding-left: 5px;
 padding-right: 5px;
 font-size:18px;
 width: auto;
 font-family: serif;
}
.output{
	color:white;
	font-size: 24px;

}
#PyLisp{
	color:white;
	font-size: 48px;
}
#PyLispUnder{
	color:white;
	font-size: 18px;
}
#Sub{
	font-size:24px;
	height: 50px;
	width:150px;
	background:#053225;
	color:white;
	border-radius: 10px;
	border: 2px solid #053225;
}
#Sub:hover{
	background:#1E463B;
	cursor:pointer;
}
#wrap1 {
	max-width:500px;
	left:0;
	right:0;
	margin:auto;
	background:#053225;
	border: 2px solid #053225;
	border-radius: 10px;
}
#wrap1:hover {
	background:#1E463B;
}
</style>

<div align = "center">
<p id="PyLisp" class="animated bounce">PyLisp</p>
<h3 id="PyLispUnder" class="animated bounceinLeft">A Simple Lisp Interpretter written in Pyton</h3>
</div>
<br><br>
<div id="wrap1">
<h3 id="info2">Sample Valid Inputs</h3>
<h4 id="info">
(+ (3)(/ 10 10))<br><br>

(- (3)(* 10 10))<br><br>

(* (2)(% 130 2)(+ 1 1 1 1)(/ 9745939781548 101912))<br><br>

( * ( 2 ) ( - 130 2 ) ( + 1 1 1 1 ) ( / 9745939781548 101912 ) )<br>
</h4>
</div>
<br><br>
<div align = "center" class="animated fadeIn">
<form action="PyLisp.php" method="post">
 <input type='text' id = "Exp" name="Expression" placeholder='Write Your Lisp Expression Here'/>
 <input type="submit" id="Sub" name="Submit" value="Evaluate"/>
</form>
</div>
</body>


<?php
    if(isset($_POST['Submit'])) {
        $Expression = "'".$_POST['Expression']."'";
        $command = escapeshellcmd('python PyLisp.py ' . $Expression);
		$output = shell_exec($command);
		echo $output;
		echo "";
	}
?>
<style>
.green{
	color:green;
}
.red {
	color:red;
}
</style>