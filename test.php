<?php
include 'fonction.php';
entete();
navbar();
?>

<body>
    <style>
        body {
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
        }

        .container {
            max-width: 800px;
            margin: 0 auto;
            display: flex;
            flex-wrap: wrap;
            justify-content: space-between;
            align-items: flex-start;
        }

        .block {
            width: 35%;
            /* Adjust as needed based on your design */
            margin-bottom: 20px;
            box-sizing: border-box;
            background-color: #3498db;
            color: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }

        @media (max-width: 600px) {
            .block {
                width: 100%;
            }
        }
    </style>



    <div class="container">
        <div class="block">Block 1</div>
        <div class="block">Block 2</div>
        <div class="block">Block 3</div>
        <div class="block">Block 4</div>
        <div class="block">Block 5</div>
        <!-- Add more blocks as needed -->
    </div>

</body>

</html>