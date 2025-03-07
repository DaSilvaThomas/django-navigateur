// On récupère les balises avec leurs id
const fullscreenButton = document.getElementById('fullscreen');
const homeContainer = document.getElementById('home-container-2');
const sortirFullscreen = document.getElementById('sortir-fullscreen');

// Passage en mode pleine écran
fullscreenButton.addEventListener('click', function() {
    if (homeContainer.requestFullscreen) {  // Général
        homeContainer.requestFullscreen();
    } else if (homeContainer.mozRequestFullScreen) { // Firefox
        homeContainer.mozRequestFullScreen();
    } else if (homeContainer.webkitRequestFullscreen) { // Chrome, Safari, Opera
        homeContainer.webkitRequestFullscreen();
    } else if (homeContainer.msRequestFullscreen) { // Internet Explorer (Edge)
        homeContainer.msRequestFullscreen();
    }

    // On cache la div fullscreen
    this.style.display = "none";

    // On affiche la div exitFullscreen
    sortirFullscreen.style.display = "flex";
});

// Sortir du mode pleine écran
sortirFullscreen.addEventListener('click', function() {
    if (document.exitFullscreen) {  // Général
        document.exitFullscreen();
    } else if (document.mozCancelFullScreen) {  // Firefox
        document.mozCancelFullScreen();
    } else if (document.webkitExitFullscreen) {  // Chrome, Safari, Opera
        document.webkitExitFullscreen();
    } else if (document.msExitFullscreen) {  // Internet Explorer (Edge)
        document.msExitFullscreen();
    }

    // On cache la div exitFullscreen
    this.style.display = "none";

    // On affiche la div fullscreen
    fullscreenButton.style.display = "flex";
});
