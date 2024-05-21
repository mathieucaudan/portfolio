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
        position: relative;
    }

    img {
        width: 100%;
    }

    /* Style pour les cards au survol */
    .w3-card:hover .card-overlay {
        display: block;
    }

    /* Style pour la balise p dans les cards */
    .card-overlay {
        display: none;
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(255, 255, 255, 0.9);
        text-align: center;
        padding: 20px;
    }
</style>


<div class="w3-container">
    <h2 style="text-align: center;">PROJETS</h2>
    <br>
    <h4 style="text-align: center;">PROJETS PERSONNELS</h4>

    <div class="w3-row">
        <div class="w3-card">
            <div class="card-overlay">
                <p>Ce site à été réalisé en collaboration avec Guillaume Cobat. Ce site à pour but d'offrir un visibilité à mon club de pentathlon</p>
            </div>
            <a href="https://cjfpentathlon-saintmalo.com/" target="_blank">
                <img src="/image/sitepenta.webp" alt="Projet 1">
            </a>
            <h2 style="text-align: center;">Site CJF Pentathlon Moderne</h2>
        </div>

        <div class="w3-card">
            <div class="card-overlay">
                <p>Ce portfolio est une étape obligatoire pour la recherche de stage/alternance. Réalisé début 2024, ce portfolio sera en constante évolution lors de mes études.</p>
            </div>
            <img src="/image/portfolio.webp" alt="Projet 2">
            <h2 style="text-align: center;">Ce portfolio</h2>
        </div>
    </div>

    <h4 style="text-align: center;">PROJETS SAE</h4>
    <div class="w3-row">
        <div class="w3-card">
            <div class="card-overlay">
                <p>L'objectif de ce projet était de nous préparer au câblage d'une salle, d'anticiper les potentiels problèmes et gérer les coûts.</p>
            </div>
            <a href="sae/sae13.pdf" target="_blank">
                <img src="/image/sae13.webp" alt="Projet 3">
            </a>
            <h2 style="text-align: center;">Câblage d’une salle TP cuivre et fibre et recettage</h2>
        </div>

        <div class="w3-card">
            <div class="card-overlay">
                <p>Ce projet m'as permis de découvrir pandas et mathlotlib afin de générer des graphiques en fonction d'un fichier csv.</p>
            </div>
            <a href="sae/sae15.py" target="_blank">
                <img src="/image/sae15.webp" alt="Projet 4">
            </a>
            <h2 style="text-align: center;">Gestion base de données en python </h2>
        </div>

        <div class="w3-card">
            <div class="card-overlay">
                <p>Ce projet en groupe de 4 à eu lieu sur 2 semaines completes, nous avions comme objectif de créer un services d'un entreprise et nous interconnecter avec les autres groupes afin de former un réseau entreprise. Nous avons construit ce réseaux, puis configuré, sécurisé puis nous l'avons attaqué grâce à une VM Kali.</p>
            </div>
            <a href="sae/sae21.pdf" target="_blank">
                <img src="/image/sae21.webp" alt="Projet 2">
            </a>
            <h2 style="text-align: center;">Construire et mettre en place un réseau
                informatique d’une petite entreprise
            </h2>
        </div>
    </div>
    <div class="w3-row">
        <div class="w3-card">
            <div class="card-overlay">
                <p>Ces différents TP m'ont permis d'accroître mes connaissances en Télécom et comprendre différentes modulation en fonction des signaux.</p>
            </div>
            <a href="sae/sae31.pdf" target="_blank">
                <img src="/image/sae31.webp" alt="Projet 2">
            </a>
            <h2 style="text-align: center;">Etudes de liens VDSL et ADSL / Mise en place de la connexion double play sur GPON (internet+TV)
            </h2>
        </div>
        <div class="w3-card">
            <div class="card-overlay">
                <p>Projet en cours!</p>
            </div>
            <a href="sae/sae303.pdf" target="_blank">
                <img src="/image/sae303.webp" alt="Projet 2">
            </a>
            <h2 style="text-align: center;">Concevoir, piloter, et sécuriser
                un réseau informatique multisites
            </h2>
        </div>
        <div class="w3-card">
            <div class="card-overlay">
                <p>Ce projet sur 8h avait pour but de découvrir le pentesting. Pour cela, un réseau comprenant un dns et un routeur de tête nous a été fournis. Nous n'avions aucune connaissance donc ce fut un projet en total autonomie. Nous avons découvert un site web, et grâce à un travail d'osint, nous avons pu nous connecté avec un compte utilisateur. Puis avec une injection sql, la base de données à été découvert et donc le mot de passe admin à été révélé. Nous avons fini par nous créer un compte admin.1-+ </p>
            </div>
            <a href="sae/pentest.pdf" target="_blank">
                <img src="/image/pentest.webp" alt="Projet 2">
            </a>
            <h2 style="text-align: center;">Pentesting sur un réseau
            </h2>
        </div>


        <div class="w3-card">
            <div class="card-overlay">
                <p>Ce projet de sécurisation avait comme objectif de mettre en place un réseau constitué d'un intranet et d'une DMZ rélié a l'internet grâce à un firewall.</p>
            </div>
            <a href="sae/sae_401.pdf" target="_blank">
                <img src="/image/sae_401.webp" alt="Projet 2">
            </a>
            <h2 style="text-align: center;">Mise en place d'un réseau sécurisé
            </h2>
        </div>
    </div>
</div>
<?php
footer();
?>