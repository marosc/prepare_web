<?php
session_start();
if (!isset($_SESSION['numeric_id'])) {
    echo "Not authorized";
    exit();
}

if (isset($_GET['path'])){
    echo file_get_contents($_GET['path']."/out.txt");
}