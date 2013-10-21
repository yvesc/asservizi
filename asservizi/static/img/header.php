<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<script src="http://code.jquery.com/jquery-2.0.3.min.js"></script>
<title>AS SERVIZI</title>
<link href="stiloso.css" rel="stylesheet" type="text/css" />
</head>
<script>
$(function(){
    $('#menux li a').on('click', function(e){
        e.preventDefault();
        var page_url=$(this).prop('href');
        $('#leftside').load(page_url);
    });
});
</script>

<script>
$(function(){
    $('#menux li a').on('mouseover', function(e){
        e.preventDefault();
        var page_url=$(this).prop('href');
        $('#leftside').load(page_url);
    });
});
</script>

<!---- SCRIPT SFONDOOOO --->

<!----------------------- ----------->

<body topmargin="0" id="body">
<!-- Header -->
<div id="sfondo"></div>
<div id="header">

<!-- TOP MENU -->
<div id="topmenu">
<div id="drop-menutop"><ul id="menutop">
	<li><a href="#">Home</a></li>
				<li><a href="#">Mission</a>
				<li><a href="#">Corporate</a></li>
				<li><a href="#">Contatti</a></li>
                </ul>
</div>
</div>


<!------------ --->
<div id="logo"></div>
</div>

<!-- Menu guida -->
<div id="contmenu">
<div id="drop-menux"><ul id="menux">
				<li class="sicurezza">><a href="menusicurezza.php">Sicurezza</br>e Salute</a></li>
				<li><a href="menuambiente.php">Ambiente</br>e Territorio</a>
				<li><a href="menuformazione.php">Formazione</br>Aziendale</a></li>
				<li><a href="menuorganizzazzione.php">Organizazzione e</br>Gestione Aziendale</a></li>
                <li><a href="menupratiche.php">Pratiche</br>Amministrative</a></li>
                <li><a href="menuperizie.php">Perizie</br>Tecnice e CTP</a></li>
			</ul>
		</div>      
        
</div>
