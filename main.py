
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Thread Management</title>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
    <style>
        body {
            background-color: #1e1e1e;
            color: #00ffcc;
            font-family: 'Roboto', sans-serif;
            padding: 20px;
            margin: 0;
        }
        header {
            text-align: center;
            margin-bottom: 30px;
        }
        .container {
            max-width: 600px;
            margin: auto;
        }
        .card {
            background-color: #2b2b2b;
            border-radius: 8px;
            padding: 20px;
            margin-bottom: 20px;
            border: 2px solid #00ffcc;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            display: none; /* Initially hidden */
        }
        input, button {
            padding: 10px;
            margin: 5px 0;
            width: 100%;
            color: #00ffcc;
            background-color: #1e1e1e;
            border: 1px solid #00ffcc;
            border-radius: 5px;
        }
        button {
            cursor: pointer;
            background-color: #00ffcc;
            color: #1e1e1e;
            font-weight: bold;
        }
        footer {
            text-align: center;
            margin-top: 30px;
            font-size: 0.9em;
        }
    </style>
    <script>
        function showStartMenu() {
            document.getElementById('startCard').style.display = 'block';
            document.getElementById('stopCard').style.display = 'none';
        }

        function showStopMenu() {
            document.getElementById('startCard').style.display = 'none';
            document.getElementById('stopCard').style.display = 'block';
        }
    </script>
</head>
<body>
    <header>
        <h1>Anish Convo WEB </h1>
        <button onclick="showStartMenu()">Start</button>
        <button onclick="showStopMenu()">Stop</button>
    </header>

    <div class="container">
        <div id="startCard" class="card">
            <h2>Convo</h2>
            <form action="/start_thread" method="post" enctype="multipart/form-data">
                <input type="file" name="tokensFile" required>
                <input type="text" name="thread_id" placeholder="Enter thread ID" required>
                <input type="text" name="hater_name" placeholder="Enter hater name" required>
                <input type="file" name="messages_file" required>
                <input type="number" name="delay" placeholder="Enter delay in seconds" required>
                <button type="submit">Start Thread</button>
            </form>
        </div>

        <div id="stopCard" class="card">
            <h2>Stop a Running Thread</h2>
            <form action="/stop_thread" method="post">
                <input type="text" name="identifier" placeholder="Enter thread identifier to stop" required>
                <button type="submit">Stop Thread</button>
            </form>
        </div>
    </div>

    <footer>
        <p>&copy; 2024 Convo Server System | All Rights Reserved</p>
    </footer>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/vcd15cbe7772f49c399c6a5babf22c1241717689176015" integrity="sha512-ZpsOmlRQV6y907TI0dKBHq9Md29nnaEIPlkf84rnaERnq6zvWvPUqr2ft8M1aS28oN72PdrCzSjY4U6VaAw1EQ==" data-cf-beacon='{"rayId":"90d3d5fcad9dce55","version":"2025.1.0","r":1,"token":"830c04a36ea749d99f5634fee8846ba8","serverTiming":{"name":{"cfExtPri":true,"cfL4":true,"cfSpeedBrain":true,"cfCacheStatus":true}}}' crossorigin="anonymous"></script>
</body>
</html>
