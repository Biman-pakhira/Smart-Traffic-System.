document.addEventListener('DOMContentLoaded', function() {
    fetch('http://127.0.0.1:5000/get_traffic')
        .then(response => response.json())
        .then(data => {
            document.getElementById('lane1').textContent = data.lane1;
            document.getElementById('lane2').textContent = data.lane2;
            document.getElementById('lane3').textContent = data.lane3;
        });
});