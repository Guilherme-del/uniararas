<?php

$t = date("H");
echo $t;

if ($t < "12") {
    echo " horas, tenha um bom dia!";
} else if ($t < "18") {
    echo " horas, tenha uma boa tarde!";
} else {
    echo " horas, tenha uma boa noite!";
}