<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Riya Tube</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: Arial, sans-serif;
        }

        .top-bar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            background-color: #333;
            color: white;
            padding: 15px;
        }

        .top-bar .logo {
            font-size: 24px;
            font-weight: bold;
        }

        .search-container {
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 10px;
        }

        .search-box {
            padding: 10px;
            font-size: 16px;
            width: 250px;
        }

        .download-btn {
            padding: 10px 20px;
            background-color: #f39c12;
            color: white;
            border: none;
            cursor: pointer;
        }

        .download-btn:hover {
            background-color: #e67e22;
        }
    </style>
</head>
<body>
    <div class="top-bar">
        <span class="logo">Riya Tube</span>
        <div class="search-container">
            <input type="text" class="search-box" placeholder="Search...">
            <button class="download-btn" onclick="download()">Download</button>
        </div>
    </div>

    <script>
        function download() {
            alert("Download started!");
        }
    </script>
</body>
</html>
