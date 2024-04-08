<!DOCTYPE html>
<html>
<head>
    <title>Register</title>
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container mt-5">
        <div class="row">
            <div class="col-md-6 offset-md-3">
                <h2 class="mb-3">Register</h2>
                <?php
             
                    $message = '';
                    if(isset($_POST['register'])) {
                        $numeric_id = $_POST['numeric_id'];
                        $password = password_hash($_POST['password'], PASSWORD_DEFAULT);

                        // Database connection
                        $conn = new mysqli('localhost', 'portal', 'password', 'portal');
                        if ($conn->connect_error) {
                            die("Connection failed: " . $conn->connect_error);
                        }

                        $stmt = $conn->prepare("INSERT INTO upload_user (`code`, `password`) VALUES (?, ?)");
                        $ok = $stmt->execute(array($numeric_id, $password));

                        if ($ok) {
                            $message = "User registered successfully!";
                        }else{
                            $message = "User registered failed!";
                        }
                        $stmt->close();
                        $conn->close();
                    }
                ?>

                <?php if($message != ''): ?>
                    <div class="alert alert-info">
                        <?php echo $message; ?>
                    </div>
                    <a href="login.php" class="btn btn-primary">Login</a>
                <?php else : ?>
                    <form action="register.php" method="post">
                        <div class="form-group">
                            <label for="numeric_id">Alphanumeric ID:</label>
                            <input type="text" class="form-control" name="numeric_id" required>
                        </div>
                        <div class="form-group">
                            <label for="password">Password:</label>
                            <input type="password" class="form-control" name="password" required>
                        </div>
                        <button type="submit" name="register" class="btn btn-primary">Register</button>
                    </form>
                <?php endif; ?>
                
            </div>
        </div>
    </div>
    <!-- Bootstrap JS and dependencies -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
