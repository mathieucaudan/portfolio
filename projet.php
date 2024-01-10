<?php
include 'fonction.php';
entete();
navbar();
?>
<style>
    .w3-container {
        max-width: 100%;
        margin: auto;
    }

    .w3-row {
        display: flex;
        flex-wrap: wrap;
        justify-content: space-around;
    }

    .w3-card {
        width: 30%;
        margin-bottom: 2%;
        padding: 0.5%;
    }

    img {
        width: 100%;
    }
</style>
<div class="w3-container">
    <h2 style="text-align: center;">PROJETS</h2>
    <br>
    <h4 style="text-align: center;">PROJETS PERSONNELS</h4>

    <div class="w3-row">
        <div class="w3-card">
            <a href="https://cjfpentathlon-saintmalo.com/" target="_blank">
                <img src="/image/site.png" alt="Projet 1">
            </a>
            <h2 style="text-align: center;">Site CJF Pentathlon Moderne</h2>
        </div>

        <div class="w3-card">
            <img src="/image/portfolio.png" alt="Projet 2">
            <h2 style="text-align: center;">Ce portfolio</h2>
        </div>
    </div>

    <h4 style="text-align: center;">PROJETS SAE</h4>
    <div class="w3-row">
        <div class="w3-card">
            <a href="sae/sae13.pdf" target="_blank">
                <img src="/image/sae13.png" alt="Projet 3">
            </a>
            <h2 style="text-align: center;">Câblage d’une salle TP cuivre et fibre et recettage</h2>
        </div>

        <div class="w3-card">
            <a href="sae/sae15.py" target="_blank">
                <img src="/image/sae15.png" alt="Projet 4">
            </a>
            <h2 style="text-align: center;">Gestion base de données en python </h2>
        </div>

        <div class="w3-card">
            <a href="sae/sae21.pdf" target="_blank">
                <img src="/image/sae21.png" alt="Projet 2">
            </a>
            <h2 style="text-align: center;">Construire et mettre en place un réseau
                informatique d’une petite entreprise
            </h2>
        </div>
    </div>
    <div class="w3-row">
        <div class="w3-card">
            <a href="sae/sae31.pdf" target="_blank">
                <img src="/image/sae31.png" alt="Projet 2">
            </a>
            <h2 style="text-align: center;">Etudes de liens VDSL et ADSL / Mise en place de la connexion double play sur GPON (internet+TV)
            </h2>
        </div>
        <div class="w3-card">
            <a href="sae/sae303.pdf" target="_blank">
                <img src="/image/sae303.png" alt="Projet 2">
            </a>
            <h2 style="text-align: center;">Concevoir, piloter, et sécuriser
                un réseau informatique multisites
            </h2>
        </div>
        <div class="w3-card">
            <a href="sae/pentest.pdf" target="_blank">
                <img src="/image/pentest.png" alt="Projet 2">
            </a>
            <h2 style="text-align: center;">Pentesting sur un réseau
            </h2>
        </div>

    </div>
</div>
<?php
footer();
