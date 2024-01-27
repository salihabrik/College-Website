document.addEventListener("DOMContentLoaded", function() {
    var navLinks = document.getElementById("navLinks");

    window.showMenu = function() {
        navLinks.style.right = "0";
    }

    window.hideMenu = function() {
        navLinks.style.right = "-200px";
    }
});



/*




document.addEventListener("DOMContentLoaded", function() {
    var navLinks = document.getElementById("navLinks");

    window.showMenu = function() {
        navLinks.style.right = "0";
    }

    window.hideMenu = function() {
        navLinks.style.right = "-200px";
    }
});*/