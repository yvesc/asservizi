<!--- MENU LEFT ------------------>
<script>
$(function(){
    $('#cssmenu li a').on('click', function(e){
        e.preventDefault();
        var page_url=$(this).prop('href');
        $('#content').load(page_url);
    });
});
</script>



<script>
$(document).ready(function(){
    var $cssmenu = $("#cssmenu li a");                
    $cssmenu.click(function(){
        $cssmenu.each(function(){
            $(this).removeClass("activecss");
        });
        $(this).addClass("activecss");                  
    });
 });
</script>

<!----------------------- ----------->

<ul id="cssmenu">
				<li><a href="dvr.php">DVR</a>
				<li><a href="dvri.php">DUVRI</a></li>
				<li><a href="pimus.php">PIMUS</a></li>
                <li><a href="psc.php">PSC</a></li>
                <li><a href="costruzione.php">Normativa</br>Macchine</a></li>
                <li><a href="costruzione.php">Certificazione</br> OHSAS 18001</a></li>
                <li><a href="costruzione.php">Gestione </br>Cantieri e Pos</a></li>
                </ul>
                
</div>