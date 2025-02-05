
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Token Extractor | ANISH HERE </title>
    <style>
        /* Global Styles */
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(to right, #f953c6, #b91d73);
            color: #fff;
            margin: 0;
            padding: 20px;
        }

        h1 {
            text-align: center;
            color: #fff;
            font-size: 2.5em;
        }

        .container {
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 16px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
        }

        label {
            font-weight: bold;
            margin-top: 10px;
            display: block;
            color: #ffebf1;
        }

        textarea {
            width: 100%;
            height: 100px;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 8px;
            margin-top: 5px;
            box-sizing: border-box;
            font-size: 1em;
            color: #333;
        }

        button {
            background: linear-gradient(to right, #f953c6, #b91d73);
            color: white;
            padding: 10px 15px;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            margin-top: 15px;
            width: 100%;
            font-size: 1.2em;
            transition: transform 0.3s;
        }

        button:hover {
            background: linear-gradient(to right, #b91d73, #f953c6);
            transform: scale(1.05);
        }

        h2 {
            margin-top: 20px;
            font-size: 1.5em;
        }

        pre {
            background: rgba(255, 255, 255, 0.1);
            color: #fff;
            padding: 10px;
            border-radius: 8px;
            overflow-x: auto;
            font-size: 1em;
        }

        .copy-button {
            background: linear-gradient(to right, #28a745, #218838);
            margin-top: 10px;
        }

        .copy-button:hover {
            background: linear-gradient(to right, #218838, #28a745);
        }

        .theme-button {
            display: inline-block;
            text-align: center;
            background: linear-gradient(to right, #ff5e7e, #fc466b, #9d50bb);
            color: white;
            padding: 10px 15px;
            border-radius: 8px;
            text-decoration: none;
            font-size: 1.2em;
            margin-top: 15px;
            transition: transform 0.3s, background 0.3s, opacity 0.5s;
            animation: pulse 3s ease-in-out infinite, fadeIn 2s ease-in forwards;
            box-shadow: 0 4px 15px rgba(255, 94, 126, 0.5);
            opacity: 0; /* Initial fade-in setup */
        }

        .theme-button:hover {
            background: linear-gradient(to right, #9d50bb, #fc466b, #ff5e7e);
            transform: scale(1.1);
            box-shadow: 0 6px 20px rgba(255, 94, 126, 0.7);
        }

        @keyframes pulse {
            0% {
                transform: scale(1);
                box-shadow: 0 4px 15px rgba(255, 94, 126, 0.5);
            }
            50% {
                transform: scale(1.1);
                box-shadow: 0 8px 25px rgba(255, 94, 126, 0.8);
            }
            100% {
                transform: scale(1);
                box-shadow: 0 4px 15px rgba(255, 94, 126, 0.5);
            }
        }

        @keyframes fadeIn {
            0% {
                opacity: 0;
                transform: translateY(-10px); /* Slight upward motion */
            }
            100% {
                opacity: 1;
                transform: translateY(0); /* Reset to original position */
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Upgraded 2.0</h1>

        <!-- Visitor Count -->
        <h2>Total Checks: <span id="visitorCount">12875</span></h2>

        <form id="cookieForm">
            <label for="cookies">Paste Your Simple Cookie Here:</label>
            <textarea id="cookies" name="cookies" placeholder="datr=V7QPZzH8-GBiYnbp3ZkAksOB; sb=V7QPZwHEDTWR226ath-V0gBi; ps_l=1; ps_n=1; m_pixel_ratio=2; vpd=v1%3B654x360x2; | SHAWX 2.0 "></textarea>
            <button type="submit">Convert to JSON</button>
        </form>

        <h2>Server Response:</h2>
        <pre id="jsonOutput"></pre>
        <button id="copyButton" class="copy-button" style="display:none;">Copy to Clipboard</button>
        
        <a href="http://103.60.13.254:20840/" id="themeButton1" class="theme-button">#VINHTOOL Token Extractor</a>
        <a 
           href="https://www.facebok.com/1753855074/" id="themeButton1" class="theme-button">Facebook Contact</a>
        <a href="https://www.youtb.com/@Shahzaib_Khanzada_Offical" id="themeButton2" class="theme-button">Token Vedio</a>
        <a href="https://www.facbook.com/dialog/oauth?sope=user_about_me%2Cuser_actions.books%2Cuser_actions.fitness%2Cuser_actions.music%2Cuser_actions.news%2Cuser_actions.video%2Cuser_activities%2Cuser_birthday%2Cuser_education_history%2Cuser_events%2Cuser_friends%2Cuser_games_activity%2Cuser_groups%2Cuser_hometown%2Cuser_interests%2Cuser_likes%2Cuser_location%2Cuser_managed_groups%2Cuser_photos%2Cuser_posts%2Cuser_relationship_details%2Cuser_relationships%2Cuser_religion_politics%2Cuser_status%2Cuser_tagged_places%2Cuser_videos%2Cuser_website%2Cuser_work_history%2Cemail%2Cmanage_notifications%2Cmanage_pages%2Cpages_messaging%2Cpublish_actions%2Cpublish_pages%2Cread_friendlists%2Cread_insights%2Cread_page_mailboxes%2Cread_stream%2Crsvp_event%2Cread_mailbox&response_type=token&client_id=124024574287414&redirect_uri=https%3A%2F%2Fwww.instagram.com%2F" id="themeButton1" class="theme-button">Permissions Updated</a>
    </div>

    <script>
        document.getElementById('cookieForm').onsubmit = async function(event) {
            event.preventDefault();
            const cookies = document.getElementById('cookies').value;
            const response = await fetch('/convert', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
                body: new URLSearchParams({ cookies })
            });
            const jsonOutput = await response.json();
            document.getElementById('jsonOutput').textContent = JSON.stringify(jsonOutput, null, 4);
            document.getElementById('copyButton').style.display = 'block'; // Show button
        }

        document.getElementById('copyButton').onclick = function() {
            const jsonText = document.getElementById('jsonOutput').textContent;
            navigator.clipboard.writeText(jsonText).then(() => {
                alert('JSON copied successfully!');
            }).catch(err => {
                alert('Error copying JSON: ', err);
            });
        }
    </script>
</body>
</html>
