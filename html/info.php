<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simulation Tool Guide</title>
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
<div class="container">
    <h1 class="mt-5">Simulation Tool</h1>

    <section class="mt-4">
        <h2>Set up</h2>

        <p>Upload stock OHLCV data to the folder. Stock data must be in CSV format (comma-separated values, not semicolon/tab/space separated) with a <code>.txt</code> file suffix. The data must have columns without a header row, with the following columns: <code>date, time, open, high, low, close, volume</code>.</p>
        <p>For example: <code>08/19/2004,11:30,2.5,2.52,2.38,2.45,147052963</code></p>
        <p><strong>IMPORTANT WARNING:</strong> If you run the input file multiple times with the same strategy name for the same stock, the output files will be overwritten.</p>
    </section>

    <section class="mt-4">
        <h2>Simulate by Actions CSV File</h2>
        <ol>
            <li>Upload actions log CSV</li>
            <li>Must be named <code>[STOCK_NAME]_[STRATEGY_NAME].csv</code>, indicating that actions in the CSV are against the stock OHLCV.</li>
            <li>Must have a header row with columns: <code>unix, date, action, operation, operation_price, operation_stop_price, price, open, high, low, close</code>.</li>
            <li>For example: <code>1484136000,2017-01-11 12:00:00,SHORT,SELL,41.34,41.46402,41.34,41.33,41.3505,41.249,41.31</code></li>

        </ol>
    </section>

    <section class="mt-4">
        <h2>Simulate by Trades CSV File</h2>
        <ol>
            <li>Upload trade log CSV </li>
            <li>Must be named <code>[STOCK_NAME]_[STRATEGY_NAME].csv</code>, indicating that trades in the CSV are against the stock OHLCV.</li>
            <li>Must have a header row with columns: <code>unix, date, trade, price, open, high, low, close</code>.</li>
            <li>For example: <code>1484136000,2017-01-11 12:00:00,SELL_BUY,41.34,41.33,41.3505,41.249,41.31</code></li>

        </ol>
    </section>

    <section class="mt-4">
        <h2>Simulate by Advices CSV File</h2>
        <ol>
            <li>Add advices log CSV </li>
            <li>Must be named <code>[STOCK_NAME]_[STRATEGY_NAME].csv</code>, indicating that advices in the CSV are against the stock OHLCV.</li>
            <li>Must have a header row with columns: <code>unix, date, advice, price, open, high, low, close</code>.</li>
            <li>For example: <code>1484136000,2017-01-11 12:00:00,1,41.34,41.33,41.3505,41.249,41.31</code></li>

        </ol>
    </section>

    <section class="mt-4">
        <h2>Simulation Results</h2>

        <p>The <code>balance.csv</code> file contains the following columns:</p>
        <ul>
            <li><code>action, operation, operation_price, operation_stop_price, unix, date, price, base, quote, debt_base, total_quote, gain</code></li>
        </ul>
        <p>This includes details such as the type of action performed, operation prices, timestamps, asset balances, and gains.</p>
    </section>
</div>

<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js"></script>
</body>
</html>
