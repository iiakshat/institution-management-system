document.getElementById('bell-icon').addEventListener('click', function() {
    document.getElementById('sidebar-notifications').classList.add('active');
    document.getElementById('overlay').classList.add('active');
});

document.getElementById('envelope-icon').addEventListener('click', function() {
    document.getElementById('sidebar-messages').classList.add('active');
    document.getElementById('overlay').classList.add('active');
});

document.getElementById('overlay').addEventListener('click', function() {
    document.getElementById('sidebar-notifications').classList.remove('active');
    document.getElementById('sidebar-messages').classList.remove('active');
    document.getElementById('overlay').classList.remove('active');
});
