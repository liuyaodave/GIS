<?php

$m = new MongoClient();
$db = $m->selectDB('google_eath');
$collection = new MongoCollection($db, 'city');

$cursor = $collection->find();

echo "<html>"

echo "<link rel='stylesheet' href='https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.3/css/bootstrap.min.css' integrity='sha384-MIwDKRSSImVFAZCVLtU0LMDdON6KVCrZHyVQQj6e8wIEJkW4tvwqXrbMIya1vriY' crossorigin='anonymous'>"

echo "<script src='https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.3/js/bootstrap.min.js' integrity='sha384-ux8v3A6CPtOTqOzMKiuo3d/DomGaaClxFYdCu2HPMBEkf6x2xiDyJ7gkXU0MWwaD' crossorigin='anonymous'></script>"

echo "<table class='table table-hover table-inverse'>"

foreach ($cursor as &$value) {
    echo "<tr>"
    echo " <th scope='row'>$cursor['id']</th>"
    echo " <td >$cursor['flatprice']</td>"
    echo " <td >$cursor['houseprice']</td>"
    echo "</tr>"
}

echo "</html>"

?>