<?php
function entete()
{
    echo "<!DOCTYPE html>
    <html>
    <head>
        <title>Portfolio Mathieu CAUDAN</title>
        <meta charset='UTF-8'>
        <meta name='viewport' content='width=device-width, initial-scale=1'>
        <link rel='stylesheet' href='https://www.w3schools.com/w3css/4/w3.css'>
        <link rel='stylesheet' href='https://fonts.googleapis.com/css?family=Amatic+SC'>
        <link rel='stylesheet' href='https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css'>
        <link rel='stylesheet' href='https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css'>

        <link rel='stylesheet' href='style/footer.css'> <!-- Ajout de la référence au fichier CSS -->
        <link rel='stylesheet' href='style/navbar.css'> <!-- Ajout de la référence au fichier CSS -->
        <script src='https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js'></script>
        <style>
        body {
            background-color: #ecf0f1;
            color : #34495e; 
        }
    </style>
     </head>";
}
function footer()
{
    echo "<div class='footer-distributed'>
    <div class='w3-half w3-container w3-center'>
        <div class='footer-center'>
            <div>
                <i class='fa fa-phone'></i>
                <p><span><a href='tel:0618694252'>06 18 69 42 52</a></p>
            </div>

            <div class='phone'>
                <i class='fa fa-envelope'></i>
                <p><span><a href='mailto:mathieucaudan@icloud.com'>mathieucaudan@icloud.com</a></p>
            </div>
        </div>
    </div>
    <div class='w3-half w3-container w3-center'>
        <div>
            <a href='https://www.linkedin.com/in/mathieu-caudan-bb882b262/' target='_blank'><img src='image/linkedin.webp' alt='Instagram' style='width: 20%; height: autp;'></a>
            <a href='https://github.com/mathieucaudan' target='_blank'><img src='image/github.webp' alt='Facebook' style='width: 20%; height: auto;'></a>
        </div>
    </div>
    <div style='color:white'><center>
        <a>© Copyright  2024 | </a>
        <a>Tous droits réservés</a>
    </center></div>
    </div>
    
    </footer>";
}


function navbar()
{
    echo "
    <div class='topnav' id='myTopnav'>
        <a href='accueil.php' class='w3-bar-item w3-button'>ACCUEIL</a>
        <a href='formation.php' class='w3-bar-item w3-button'>FORMATION</a>
        <a href='competence.php' class='w3-bar-item w3-button'>COMPETENCES</a>
        <a href='projet.php' class='w3-bar-item w3-button'>PROJETS</a>
        <a href='loisir.php' class='w3-bar-item w3-button'>LOISIRS</a>
        <a href='javascript:void(0);' class='icon' onclick='toggleMenu()'>
            <i class='fa fa-bars'></i>
        </a>
    </div>
    
    <script>
    function toggleMenu() {
        var x = document.getElementById('myTopnav');
        if (x.className.indexOf('responsive') === -1) {
            x.className += ' responsive';
        } else {
            x.className = x.className.replace(' responsive', '');
        }
    }
    
    </script>";
}
