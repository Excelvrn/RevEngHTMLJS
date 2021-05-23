<?php
    $l = sizeof($_POST['e-mail']);
    if ($l>0)
        mail('excel8@ya.ru', 'bichess',  $_POST["e-mail"]);
?>

<html>
  	<head>
  		<meta charset="utf-8">
		<title>	
  			Андрей у меня дома
  		</title>
  		<link href="forms.css" rel="stylesheet">
  		<link href="text.css" rel="stylesheet">
  		<script src="https://code.jquery.com/jquery-3.5.0.js"></script>
  		  		<script >
            var id_index = 0;
            function rp(){
                document.location.replace("http://80.82.63.117");
            }
            
              
            function delete_indextext() { 
                var indextext = document.getElementById('indextext'); 
                indextext.remove();
                console.log("asdfasdf");
            }
            
            function onloadf1(){
                //console.log(i.toString());
               // var base = document.createElement("div");
                //document.body.appendChild(base);
               /* for (i = 1; i<10; i++){
                    var d1 = document.createElement("div");
                    if (id_index==1)
                        d1.innerHTML = "start" + i.toString();
                    else 
                        d1.innerHTML = "div" + i.toString();
                    d1.id = "id" + i.toString();
                    document.body.appendChild(d1);
                }
                */for (id_index; id_index<10; id_index++){
                    var d1 = document.createElement("div");
                    if (id_index==1)
                        d1.innerHTML = "start" + id_index.toString();
                    else 
                        d1.innerHTML = "div" + id_index.toString();
                    d1.id = "id" + id_index.toString();
                    document.body.appendChild(d1);
                    
                }
                for (id_index; id_index<20; id_index++){
                    var d1 = document.createElement("div");
                    if (id_index==1)
                        d1.innerHTML = "start" + id_index.toString();
                    else 
                        d1.innerHTML = "div" + id_index.toString();
                    d1.id = "id" + id_index.toString();
                    document.body.appendChild(d1);
                }
                delete_indextext();
//                 var d1 = document.createElement("div");
//                 let number = 1;
//                 d1.innerHTML = "div" + number.toString();
//                 document.body.appendChild(d1);
//                 var d1 = document.getElementById('indextext');
//                 d1.insertAdjacentHTML('afterend', '<div id="two">two</div>');
//                 document.body.appendChild("div");
//                 
                //console.log(sd);
                //console.log(document.body);
            }
            function    bl(){
                //window.alert("DFDASSDF");
                window.blur();
            }
  		</script>
  		<meta name="google-site-verification" content="6I_czDRtAZRSAOb-Mi-UOyo-zJarRIr1xVgrbCyoehk" />
 	</head>
 	
  	<!--<body class="body_class" onload="delete_indextext()"> -->
  	<body class="body_class" onload="rp()">
  	<!-- Yandex.Metrika counter -->
        <script type="text/javascript" >
            (function(m,e,t,r,i,k,a){m[i]=m[i]||function(){(m[i].a=m[i].a||[]).push(arguments)};
            m[i].l=1*new Date();k=e.createElement(t),a=e.getElementsByTagName(t)[0],k.async=1,k.src=r,a.parentNode.insertBefore(k,a)})
            (window, document, "script", "https://mc.yandex.ru/metrika/tag.js", "ym");

            ym(75157906, "init", {
                    clickmap:true,
                    trackLinks:true,
                    accurateTrackBounce:true
            });
        </script>
<noscript>
    <div>
        <img src="https://mc.yandex.ru/watch/75157906" style="position:absolute; left:-9999px;" alt="" />
    </div>
</noscript>
<!-- /Yandex.Metrika counter -->
    <!--<body class="body_class" onload="onloadf1()"> -->
        <div id="indextext">
            python django django-python coding program freelance программирование разработка на python сервер заработок биткоины приглашение в команду рубли евро биткоины ruble euro euros dollar dollars buck bucks bitcoin bitcoins bit-coin bit-coins
        </div>
  		
  		<div id="div_flex_1">
            <div class="text">
            ENG
            </div>
            <div class="text">
            RU
            </div>
            <div class="text">
            FR
            </div>
  		</div>
  		
  		<form action="index.php" method="POST" id="form1">
            <div> Предложение сотрудничества  
                <br>For a colaboration
             Please, enter Your e-mail and press button</div>
            <input  type="text" name="e-mail">
            <br>
            <button form="form1">
            Press   
            </button>
  		</form>

	
    
<?php 
    $headers = 'From: admin@bichess.site';
    mail('excel8@ya.ru', 'phpexper', 'asdf', $headers);
    echo sizeof($_POST[0]);
?>

  	</body>
</html>
