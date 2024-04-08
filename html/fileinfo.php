<?php
session_start();
if (!isset($_SESSION['numeric_id'])) {
    echo "Not authorized";
    exit();
}

function analyzeCsv($filePath) {
    $handle = fopen($filePath, 'r');
    if (!$handle) {
        return "Cannot open file: $filePath";
    }

    $dates = []; // Array to store all the dates and times

    // Skip the header line
    fgetcsv($handle);

    // Read each line of the CSV
    while (($data = fgetcsv($handle)) !== FALSE) {
        // Assuming the date and time are in the second column (index 1)
        $dates[] = strtotime($data[1]); // Convert date and time to timestamp and store it
    }

    fclose($handle);

    if (count($dates) < 2) {
        return "Need at least two data points to determine frequency.";
    }

    // Calculate the frequency by subtracting the first timestamp from the second
    $frequencySeconds = $dates[1] - $dates[0];

    // Convert frequency to a human-readable format
    if ($frequencySeconds == 1800) {
        $frequency = "30 minutes";
    } elseif ($frequencySeconds == 3600) {
        $frequency = "1 hour";
    } elseif ($frequencySeconds == 86400) {
        $frequency = "1 day";
    } else {
        $frequency = "$frequencySeconds seconds";
    }

    // Convert the first and last timestamp back to the date and time format
    $firstDate = date('d. m. Y H:i:s', $dates[0]);
    $lastDate = date('d. m. Y H:i:s', end($dates));

    return $firstDate.' - '.$lastDate . ' [freq. '.$frequency.']';
}

function analyzeCsvWithDifferentFormat($filePath) {
    $handle = fopen($filePath, 'r');
    if (!$handle) {
        return "Cannot open file: $filePath";
    }

    $timestamps = []; // Array to store all the timestamps

    // Read each line of the CSV
    while (($data = fgetcsv($handle)) !== FALSE) {
        // Combine the date and time into one string
        // Assuming date is in the first column (index 0) and time is in the second column (index 1)
        $dateTime = DateTime::createFromFormat('m/d/Y,H:i', $data[0] . ',' . $data[1]);
        if ($dateTime === false) {
            // Handle error in date/time format
            continue; // Skip to the next iteration
        }
        $timestamps[] = $dateTime->getTimestamp(); // Convert to timestamp and store it
    }

    fclose($handle);

    if (count($timestamps) < 2) {
        return "Need at least two data points to determine frequency.";
    }

    // Calculate the frequency by subtracting the first timestamp from the second
    $frequencySeconds = $timestamps[1] - $timestamps[0];

    // Convert frequency to a human-readable format
    $frequency = calculateFrequencyStock($frequencySeconds);

    // Convert the first and last timestamp back to the date and time format
    $firstDate = date('Y-m-d H:i:s', $timestamps[0]);
    $lastDate = date('Y-m-d H:i:s', end($timestamps));

    return $firstDate.' - '.$lastDate . ' [freq. '.$frequency.']';
}

function calculateFrequencyStock($seconds) {
    switch ($seconds) {
        case 1800:
            return "30 minutes";
        case 3600:
            return "1 hour";
        // Add more cases as needed
        default:
            if ($seconds % 86400 == 0) {
                $days = $seconds / 86400;
                return "$days day" . ($days > 1 ? "s" : "");
            } elseif ($seconds % 3600 == 0) {
                $hours = $seconds / 3600;
                return "$hours hour" . ($hours > 1 ? "s" : "");
            } elseif ($seconds % 60 == 0) {
                $minutes = $seconds / 60;
                return "$minutes minute" . ($minutes > 1 ? "s" : "");
            } else {
                return "$seconds seconds";
            }
    }
}


if (isset($_GET['filepath'], $_GET['classic'])){
    echo analyzeCsv($_GET['filepath']);
}
if (isset($_GET['filepath'], $_GET['special'])){
    echo analyzeCsvWithDifferentFormat($_GET['filepath']);
}