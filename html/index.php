<?php
session_start();
if (!isset($_SESSION['numeric_id'])) {
    header("Location: login.php"); // Redirect to login if not logged in
    exit();
}

function getQueryPath($params){
    $q = "?";
    $x = array();
    foreach ($_GET as $key=>$value) {
        $x[$key] = $value;
    }
    foreach ($params as $key=>$value) {
        $x[$key] = $value;
    }
    foreach ($x as $key=>$value){
        if ($q!="?"){
            $q.="&";
        }
        $q.=$key."=".$value;
    }
    return $q;
}

function getConfig($userid, $data)
{
    if ($data['expname']==null){
        $data['expname'] = 'exp';
    }

    if ($data['price_type']==null){
        $data['price_type'] = 'ACTUAL_CLOSE';
    }

    if ($data['input_folder'] == null){
        $data['input_folder'] = "uploads/".$userid."/";
    }
    $exp_name = $data['expname']."-".time();

    $config = [
        "EXPERIMENT_NAME" => $userid."/".$exp_name,
        "BASE_STOCK_TXT_FILES_PATH" => $data['input_folder'] ."stocks/",
        "LOAD_STOCKS" => $data['stocks_prepare'] == null ? [] : $data['stocks_prepare'],
        "SIMULATION_CURRENT_PRICE_TYPE" => $data['price_type'],

        "INPUT_FILTER_TIME_START" => $data['startTime'] == null ? "09:30:00" : $data['startTime'],
        "INPUT_FILTER_TIME_END" => $data['endTime'] == null ? "15:30:00" : $data['endTime'],
        "INPUT_FILTER_DATE_START" => $data['startDate'] == null ? "2020-01-01" : $data['startDate'],
        "INPUT_FILTER_DATE_END" => $data['endDate'] == null ? "2022-12-31" : $data['endDate'],

    ];

    $exp_log = "results/".$config["EXPERIMENT_NAME"];
    if (!file_exists($exp_log)) {
        mkdir($exp_log, 0777, true);
    }

    $jsonData = json_encode($config, JSON_PRETTY_PRINT);
    $jsonPath = 'uploads/' . $userid . '/config.json';
    if (!file_exists( 'uploads/' . $userid )) {
        mkdir('uploads/' . $userid , 0777, true);
    }
    file_put_contents($jsonPath, $jsonData);
    //$output = shell_exec("python3 /home/code/simulate_models.py /var/www/html/" . $jsonPath . " 2>&1");
    $output = shell_exec("python3 -u /home/code/prepare_data.py /var/www/html/" . $jsonPath . " > /var/www/html/".$exp_log."/out.txt 2>&1 &");
    header("Location: index.php".getQueryPath(array('exp_result'=>$exp_name)));
    exit();
}

$numeric_id = $_SESSION['numeric_id'];
$message = "";
$log_text = "";

if (isset($_POST['run'])) {
    getConfig($numeric_id,$_POST);
}

if (isset($_FILES['stocks'])) {

    $numeric_id = $_SESSION['numeric_id'];

    // Create directory if it doesn't exist
    if (!file_exists("uploads/" . $numeric_id)) {
        mkdir("uploads/" . $numeric_id, 0777, true);
    }

    $target_dir = "uploads/" . $numeric_id . "/stocks/";

    // Create directory if it doesn't exist
    if (!file_exists($target_dir)) {
        mkdir($target_dir, 0777, true);
    }

    foreach ($_FILES['stocks']['name'] as $i => $name) {
        if (strlen($_FILES['stocks']['name'][$i]) > 1) {
            if (move_uploaded_file($_FILES['stocks']['tmp_name'][$i], $target_dir . $name)) {
                $message .= "Stocks uploaded: " . $name . "<br>";
            } else {
                $message .= "Failed to upload file: " . $name . "<br>";
            }
        }
    }
}

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Dashboard</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="dist/js/jquery-3.7.1.js"></script>
    <link href="dist/css/bootstrap.min.css" rel="stylesheet">
    <script src="dist/js/bootstrap.bundle.min.js"></script>


    <style>

        .row {
            padding-top: 20px;
        }


        #datacol {
            height: 90vh; /* 100% of the viewport height */
            overflow-y: auto; /* Enables vertical scrolling */
        }

    </style>
    <style>
        .gallery img {
            width: 100%;
            height: auto;
            display: block; /* Ensures no extra space around the image */
        }

        .desc {
            padding: 15px;
            text-align: center;
        }
    </style>
    <script>
        function loadinfo(id, path){
            $.ajax( "fileinfo.php?filepath="+path+"&classic" )
                .done(function(value) {
                    $("#"+id).html(value);
                })
                .fail(function() {
                    $("#"+id).html("error");
                });
        }
        function loadstockinfo(id, path){
            $.ajax( "fileinfo.php?filepath="+path+"&special" )
                .done(function(value) {
                    $("#"+id).html(value);
                })
                .fail(function() {
                    $("#"+id).html("error");
                });
        }
    </script>
</head>
<body>
<div class="container-fluid">

    <div class="row">
        <div class="col-12 col-lg-8">
            <h4 style="display: inline;">Welcome <?php echo $numeric_id; ?>
            </h4>
            <a href="logout.php" style="margin-bottom: 10px; margin-left: 50px;" class="btn btn-primary">Logout</a>

            <a href="info.php" style="margin-bottom: 10px; margin-left: 50px;" class="btn">Documentation</a>
            <br>
            <hr  style="margin-bottom: 50px;"/>


            <?php
            if (isset($_GET['exp_result'])){
                $experiment_result = $_GET['exp_result'];
                $experiment_result_path = "results/" . $numeric_id . '/'.$experiment_result;
//                $userFiles = array_filter(glob($userDir . '/*'), 'is_dir');
                //foreach (array_reverse($userFiles) as $filePath) {
                echo '<h4>Experiment '.$experiment_result
                    .' <button class="btn btn-light" onclick="$(\'#user-config-'.$experiment_result.'\').toggle();">config</button>'
                    .' <button class="btn btn-light" onclick="$(\'#full-config-'.$experiment_result.'\').toggle();">full config</button>'
                    .' <button class="btn btn-light" onclick="$(\'#runlog-'.$experiment_result.'\').toggle();">log</button>'
                    .' <button class="btn btn-light" onclick="loadlog();">refresh log</button>'
                    .'</h4>';

                $logt = file_get_contents($experiment_result_path."/out.txt");
                $logtstyle= "";
//                if (strpos($logt, "==FINISHED==") !== false){
//                    $logtstyle = " style='display:none;'";
//                }
                echo '<div class="alert alert-info" id="runlog-'.$experiment_result.'"'.$logtstyle.'><pre>'.$logt.'</pre></div>';

                $json = file_get_contents($experiment_result_path."/log/user_config.json");
                $json_data = json_decode($json,true);
                echo "<pre id='user-config-".$experiment_result."' style='display: none'><code>";
                print_r($json);
                echo "</code></pre>";

                $json = file_get_contents($experiment_result_path."/log/full_config.json");
                $json_data = json_decode($json,true);
                echo "<pre id='full-config-".$experiment_result."' style='display: none'><code>";
                print_r($json);
                echo "</code></pre>";

                echo '<div class="container-fluid mt-5"><div class="row">';

                $experimentDir = $experiment_result_path. "/simulation/balance/data";
                $experimentFiles = array_filter(glob($experimentDir . '/*'), 'is_dir');
                foreach ($experimentFiles as $stockPath) {
                    $experimentStockFiles = array_filter(glob($stockPath . '/*'), 'is_dir');
                    foreach ($experimentStockFiles as $plotPath) {
                        $file = basename($plotPath);
                        $relativeFilePath = $plotPath . "/gain.png"; // Construct the relative file path
                        $fileDate = htmlspecialchars($file);

                        //echo "<a href='$relativeFilePath'><img alt='$fileDate' src='$relativeFilePath' class='img-responsive'/></a>";
                        echo '<div class="col-lg-6 col-md-12 col-sm-12 mb-6">'; // Adjusted column classes
                        echo '<div class="gallery">';
                        echo '<a name="' . $file . '" target="_blank" href="' . $relativeFilePath . '">';
                        echo '<img src="' . $relativeFilePath . '" alt="' . $fileDate . '" style="width:100%">';
                        echo '</a>';
                        echo '<div class="desc">' . $fileDate . '</div>'; // Sets the filename as the caption
                        echo '</div>';
                        echo '</div>';
                    }

                }
                if (sizeof($experimentFiles) == 0) {
                    echo "<p>Ziadne data</p>";
                }
                echo '</div></div><hr/>';

            }
            ?>

        </div>
        <div id="datacol" class="col-12 col-lg-4">

            <?php if ($message != '' || $log_text != ''): ?>
                <div class="alert alert-info" id="loginfo">
                    <h4>Log</h4>
                    <?php echo $message; ?>
                    <br>
                    <?php echo $log_text; ?>
                    <a href="#"  class="btn btn-primary" onclick="$('#loginfo').hide();">Close</a>
                </div>
            <?php endif; ?>


            <h3>Upload data</h3>
            <p class="mt-4">
                <a class="btn btn-light" href="#" onclick="showElement('upload-stocks')"><strong>Upload stocks</strong></a>
            </p>

            <div style="display: none" id="upload-stocks">
                <form method="post" enctype="multipart/form-data">

                    <div class="form-group">
                        <input style="width: 250px;" type="file" name="stocks[]" multiple class="form-control">
                    </div>
                    <button type="submit" name="submit" class="btn btn-primary">upload stocks</button>
                </form>

            </div>


            <?php
            $exp_dir =  "uploads/" . $numeric_id ;
            $exp_root = "results/".$numeric_id;
            $exp_name = "uploads";
            $stock_custom_dir =  "uploads/" . $numeric_id . "/stocks";
            $title = "";

            if (isset($_GET['experiment'], $_GET['experiment_folder'])){
                $exp_root =  "other/".$_GET['experiment_folder'];
                $exp_dir = $exp_root."/".$_GET['experiment']."/";
                $exp_name = $_GET['experiment'];
                $title = $_GET['experiment_folder']."/".$_GET['experiment'];
                $stock_custom_dir = $exp_root."/".$_GET['experiment']."/stocks";
            }
            if (isset($_GET['stocks_folder'])){
                $stock_custom_dir = $_GET['stocks_folder'];
            }

            $stock_files = array();
            $dataFiles = array_filter(glob($stock_custom_dir . '/*'));

            foreach ($dataFiles as $filePath) {
                $file = basename($filePath);
                if (strtolower(pathinfo($file, PATHINFO_EXTENSION)) == "txt") {
                    array_push($stock_files, $filePath);
                }
            }



            ?>
            <hr>

            <h3>Experiment results  <a class="btn btn-light" href="#" onclick="$('#experiments-results').toggle()"><small>toggle</small></a></h3>
            <div id="experiments-results" style="display: none">

                <?php
                $_expFolders = array_filter(glob( 'results/*'), 'is_dir');
                foreach ($_expFolders as $_expFolder) {
                    echo "<strong>".basename($_expFolder)."</strong><br>";
                    $_expNames = array_filter(glob( $_expFolder.'/*'), 'is_dir');
                    foreach ($_expNames as $_expName) {
                        echo "<div class='list-group-item list-group-item-action'><a href='".getQueryPath(array("exp_result"=>basename($_expName)))."'>"
                            . basename($_expName)
                            . "</a></div>";

                    }
                }
                ?>
            </div>
            <hr>

            <h3>Experiment sources<a class="btn btn-light" href="#" onclick="$('#experiments-list').toggle()"><small>toggle</small></a></h3>
            <div id="experiments-list" style="display: none">
                <div class='list-group-item list-group-item-action'><a href='index.php'>From my uploads</a></div>
                <br><br>

                <?php
                $_expFolders = array_filter(glob( 'other/*'), 'is_dir');
                foreach ($_expFolders as $_expFolder) {
                    echo "<strong>".basename($_expFolder)."</strong><br>";
                    $_expNames = array_filter(glob( $_expFolder.'/*'), 'is_dir');
                    foreach ($_expNames as $_expName) {
                        if (!file_exists($_expName."/stocks")){
                            continue;
                        }
                        echo "<div class='list-group-item list-group-item-action'><a href='".getQueryPath(array("experiment"=>basename($_expName),"experiment_folder"=> basename($_expFolder)))."'>"
                            . basename($_expName)
                            . "</a></div>";

                    }
                }
                ?>
            </div>
            <hr>
            <div style="margin-right: 50px;">
                <h3>Preparation TFT<a class="btn btn-light" href="#" onclick="$('#simulate-form').toggle()"><small>toggle</small></a></h3>
                <strong><?php echo $title; ?></strong>
                <br><br>
                <form method="post" id="simulate-form" action="index.php<?php echo getQueryPath(array());?>">
                    <div class="form-group">

                        <?php
                        //echo $exp_dir;
                        if (isset($_GET['experiment'], $_GET['experiment_folder'])){
                            echo '<input type="hidden" name="input_folder" value="'.$exp_dir.'" >';
                        }
                        ?>
                    </div>

                    <div class="form-group row">
                        <label for="expname" class="col-sm-2 col-form-label">Experiment name<br><small>can be empty</small></label>
                        <div class="col-sm-10">
                            <input type="text" class="form-control" id="expname" name="expname">
                        </div>
                    </div>




                    <hr>
                    <div class="form-group row">
                        <strong>Stock</strong>
                    </div>


                    <div class="form-group stock-section">
                        <label for="startDate">From Date:</label>
                        <input type="date" id="startDate" name="startDate" value="2020-01-01">
                    </div>

                    <div class="form-group stock-section">
                        <label for="endDate">To Date:</label>
                        <input type="date" id="endDate" name="endDate" value="2022-12-31">
                    </div>
                    <div class="form-group stock-section">
                        <label for="startTime">Start Time (each day start at):</label>
                        <input type="time" id="startTime" name="startTime" step="1" value="09:30:00">
                    </div>

                    <div class="form-group stock-section">
                        <label for="endTime">End Time (each day end at):</label>
                        <input type="time" id="endTime" name="endTime" step="1" value="15:30:00">
                    </div>

                    <div class="form-group row stock-section">

                            <legend class="col-form-label col-sm-2 pt-0">Simulated price</legend>
                            <div class="col-sm-10">
                                <div class="form-check">
                                    <input class="form-check-input" type="radio" name="price_type" id="price_type1" value="ACTUAL_CLOSE" checked>
                                    <label class="form-check-label" for="price_type1">
                                        Actual close price
                                    </label>
                                </div>
                                <div class="form-check">
                                    <input class="form-check-input" type="radio" name="price_type" id="price_type2" value="NEXT_OPEN">
                                    <label class="form-check-label" for="price_type2">
                                        Next open price
                                    </label>
                                </div>
                            </div>
                    </div>

                    <div class="form-group row">

                        <div class="col-sm-2">OHLCV</div>
                        <div class="col-sm-10">
                            <p class="btn btn-secondary" onclick="$('.prepare_checkbox').prop('checked', true)">Check all</p>
                            <p class="btn btn-secondary" onclick="$('.prepare_checkbox').prop('checked', false)">Uncheck all</p>
                        </div>
                        <div class="col-sm-10">

                            <?php
                            foreach ($stock_files as $file_i) {
                                $option = basename($file_i,".txt");
                                $stockDir = str_replace(basename($file_i),"", $file_i);
                                //$fileinfo = analyzeCsvWithDifferentFormat($stockDir.$option.".txt");
                                echo '<div class="form-check">
                                        <input class="form-check-input prepare_checkbox" type="checkbox" name="stocks_prepare[]" value="' . $option . '" id="stock-' . $option . '">
                                        <label class="form-check-label" for="stock-' . $option . '">
                                            ' . $option . '
                                        </label>
                                        <small class="stock-info-load" id="info-stock-' . $option . '"></small>
                                        <a target="_blank" href="'.$stockDir.$option.'.txt"><small>download</small></a>
                                        <script>loadstockinfo("info-stock-' . $option . '","'.$stockDir.$option.'.txt")</script>
                                      </div>';

                            }
                            ?>
                        </div>
                    </div>




                    <hr>
                    <button type="submit" name="run" class="btn btn-primary">Run</button>
                </form>
            </div>


        </div>

    </div>


</div>



<script>
    function showElement(id) {
        $("#upload-advices").hide();
        $("#upload-trades").hide();
        $("#upload-actions").hide();
        $("#upload-stocks").hide();

        $("#" + id).show();
    }

    function showList(id) {
        $("#" + id).toggle();
    }

    <?php if (isset($_GET['exp_result'])):
        $logt = file_get_contents("results/" . $numeric_id . '/' . $_GET['exp_result']."/out.txt");
        if (strpos($logt, "==FINISHED==") === false) : ?>
            $(document).ready(function(){
                var intervalId = setInterval(function() {
                    $.ajax({
                        url: '<?php echo "status.php?path=results/" . $numeric_id . '/' . $_GET['exp_result'] . ''; ?>&t=' + Date.now(),
                        type: 'GET',
                        success: function (data) {
                            if (data.trim().endsWith("==FINISHED==")) {
                                // If it does, stop the interval
                                clearInterval(intervalId);
                                location.reload();
                            }
                            // Display the content in the element with id "log"
                            $('#runlog-<?php echo $_GET['exp_result'];?>').html("<pre>" + data + "</pre>");
                        },
                        error: function () {
                            $('#runlog-<?php echo $_GET['exp_result'];?>').text('Error loading the file');
                        }
                    });
                },2000);
            });
        <?php endif; ?>
    <?php endif; ?>

    function loadlog(){
        <?php if (isset($_GET['exp_result'])): ?>
            $.ajax({
                url: '<?php echo "status.php?path=results/" . $numeric_id . '/'. $_GET['exp_result'].''; ?>&t='+Date.now(),
                type: 'GET',
                success: function(data) {
                    // Display the content in the element with id "log"
                    $('#runlog-<?php echo $_GET['exp_result'];?>').html("<pre>"+data+"</pre>");
                },
                error: function() {
                    $('#runlog-<?php echo $_GET['exp_result'];?>').text('Error loading the file');
                }
            });
        <?php endif; ?>
    }

</script>


</body>
</html>
