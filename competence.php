<?php
include 'fonction.php';
entete();
navbar();
?>
<div class="w3-container" style="color:white">
    <h2>
        <center>COMPETENCES</center>
    </h2>
    <div class="w3-quarter w3-container w3-center">
        <h3>Languages de programmation</h3>
        <div class="cards">
            <div class="card">
                <img style="height: calc(2vw + 40px);" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/java/java-original-wordmark.svg" />
            </div>
            <div class="card">
                <img style="height: calc(2vw + 40px);" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original-wordmark.svg" />
            </div>
            <div class="card">
                <img style="height: calc(2vw + 40px);" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original-wordmark.svg" />
            </div>
            <div class="card">
                <img style="height: calc(2vw + 40px);" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mysql/mysql-original-wordmark.svg" />
            </div>
            <div class="card">
                <img style="height: calc(2vw + 40px);" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/php/php-plain.svg" />
            </div>
            <div class="card">
                <img style="height: calc(2vw + 40px);" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original-wordmark.svg" />
            </div>
        </div>

    </div>
    <div class="w3-quarter w3-container w3-center">
        <h3>Réseaux</h3>
        <div class="cards">
            <div class="card">
                <img style="height: calc(2vw + 40px);" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/apache/apache-original.svg" />
            </div>
            <div class="card">
                <img style="height: calc(2vw + 40px);" src="/image/cisco.png" />
            </div>
            <div class="card">
                <img style="height: calc(2vw + 40px);" src="/image/mpls.png" />
            </div>
            <div class="card">
                <img style="height: calc(2vw + 40px);" src="/image/ospf.png" />
            </div>
        </div>
    </div>
    <div class="w3-quarter w3-container w3-center">
        <h3>Télécom</h3>
        <div class="cards">
            <div class="card">
                <img style="height: calc(2vw + 40px);" src="/image/xdsl.png" />
            </div>
            <div class="card">
                <img style="height: calc(2vw + 40px);" src="/image/ftth.png" />
            </div>
        </div>
    </div>
    <div class="w3-quarter w3-container w3-center">
        <h3>Divers</h3>
        <div class="cards">
            <div class="card">
                <img style="height: calc(2vw + 40px);" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linux/linux-original.svg" />
            </div>
            <div class="card">
                <img style="height: calc(2vw + 40px);" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/android/android-original-wordmark.svg" />
            </div>
            <div class="card">
                <img style="height: calc(2vw + 40px);" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vscode/vscode-original-wordmark.svg" />
            </div>
            <div class="card">
                <img style="height: calc(2vw + 40px);" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original-wordmark.svg" />
            </div>
        </div>
    </div>

</div>
<br>
<br>
<h2 style="color :white">
    <center>La plupart de ces compétences ont été acquises lors de mes études. J'essaie maintenant d'en développer certaines de manière autonome, à l'image de mes efforts avec le langage Python.</center>
</h2>

<style>
    .cards {
        display: flex;
        flex-wrap: wrap;
    }

    .card {
        flex-grow: 1;
    }
</style>
<?php
footer();
