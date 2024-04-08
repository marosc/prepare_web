<?php
//error_reporting(0);

try {
    $headers = getallheaders();
        
    $apikey = isset($headers["x-apikey"]) ? $headers["x-apikey"] : "";
    if ($apikey==""){
        throw new Exception("Api key required",400);
    }

    if ($apikey!="mvx0dtrEknr53uEozm1Czf8oCvnxyIPpkB1Up2p6PK"){
        throw new Exception("Api invalid",401);
    }

    $json = file_get_contents('php://input');

    if ($_SERVER['REQUEST_METHOD'] !== "POST") {
        throw new Exception("User id and password required",400);
    }

    $data = json_decode($json, true);

    if (!isset($data['code']) ||  !isset($data['password'])){
        throw new Exception("User id and password required",400);
    }

    $code = $data['code'];
    $password = $data['password'];

    if ($code=="" || $password==""){
        throw new Exception("User id and password can't be empty",400);
    }

    $conn = new mysqli('localhost', 'portal', 'password', 'portal');
    if ($conn->connect_error) {
        throw new Exception("Database error. Try again later. ".$conn->connect_error,500);
    }

    $stmt = $conn->prepare("SELECT code, password FROM upload_user WHERE code = ?");
    $stmt->bind_param("s", $code);
    $stmt->execute();
    $result = $stmt->get_result();

    $message = "Failed to login. Try again later.";
    if ($result->num_rows > 0) {
        $row = $result->fetch_assoc();
        if (password_verify($password, $row['password'])) {
            $message = "";
        } else {
            $message =  "Invalid password!";
        }
    } else {
        $message =  "User not found!";
    }

    $stmt->close();
    $conn->close();

    http_response_code(200);
    echo json_encode(array("status"=> $message));

}catch (Exception $exception){
    http_response_code($exception->getCode());
    echo json_encode(array("status"=> $exception->getMessage()));
}

?>