
function openPage(code) {

    switch (code) {
    case 0:
        window.open('http://deft-idiom-105001.appspot.com', '_blank');
        console.log("Shooting to noteapp")
        break;
    case 1:
        window.open('http://www.google.com', '_blank');
        console.log("Going to google.")
        break;
    case 2:
        window.open('http://www.udacity.com', '_blank');
        break;
    case 3:
        window.open('http://www.hotschedules.com');
        break;
    case 4:
        document.location.href = "/secondpage";
        break;
    case 5:
        document.location.href = "/";
        break;
    }
}



