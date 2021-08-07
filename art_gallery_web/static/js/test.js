function myFunction() {
    if (document.getElementById("my-profile").style.display === 'block') {

        document.getElementById("my-profile").style.display = 'none';
        document.getElementById("btn-profile").innerText = 'Your Portfolio';
    }
    else {
        document.getElementById("my-profile").style.display = 'block';
        document.getElementById("btn-profile").innerText = ' Close Your Portfolio';
    }
}