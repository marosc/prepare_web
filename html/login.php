<!-- Similar structure to register.php, but for login -->
<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container mt-5">
        <div class="row">
            <div class="col-md-6 offset-md-3">
                <h2 class="mb-3">Login</h2>
                <?php
                    $message = '';
                    if(isset($_POST['login'])) {
                        $numeric_id = $_POST['numeric_id'];
                        $password = $_POST['password'];

                        $conn = new mysqli('localhost', 'portal', 'password', 'portal');
                        if ($conn->connect_error) {
                            die("Connection failed: " . $conn->connect_error);
                        }

                        $stmt = $conn->prepare("SELECT code, password FROM upload_user WHERE code = ?");
                        $stmt->bind_param("s", $numeric_id);
                        $stmt->execute();
                        $result = $stmt->get_result();

                        if ($result->num_rows > 0) {
                            $row = $result->fetch_assoc();
                            if (password_verify($password, $row['password'])) {
                                session_start();
                                $_SESSION['numeric_id'] = $numeric_id;
                                // Redirect to user's dashboard
                                header("Location: index.php");
                            } else {
                                $message =  "Invalid password!";
                            }
                        } else {
                            $message =  "User not found!";
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
                <?php endif; ?>
                <form action="login.php" method="post">
                    <div class="form-group">
                        <label for="numeric_id">Alphanumeric ID:</label>
                        <input type="text" class="form-control" name="numeric_id" required>
                    </div>
                    <div class="form-group">
                        <label for="password">Password:</label>
                        <input type="password" class="form-control" name="password" required>
                    </div>
                    <button type="submit" name="login" class="btn btn-primary">Login</button>
                </form>
                <hr>
                <a href="register.php" >Create account</a>
            </div>
        </div>

    </div>
    <!-- Bootstrap JS and dependencies -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
