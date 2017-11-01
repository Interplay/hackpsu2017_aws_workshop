$(document).ready(function() {
    $('#checkin').modal();
});

$(document).ready(function() {
    var btn = document.getElementById('index');
    var clipboard = new Clipboard(btn);
    clipboard.on('success', function(e) {
        console.log(e);
    });
    clipboard.on('error', function(e) {
        console.log(e);
    }); 
});

$(document).ready(function() {
    var btn = document.getElementById('s3policy');
    var clipboard = new Clipboard(btn);
    clipboard.on('success', function(e) {
        console.log(e);
    });
    clipboard.on('error', function(e) {
        console.log(e);
    }); 
});

$(document).ready(function() {
    var btn = document.getElementById('ec2policy');
    var clipboard = new Clipboard(btn);
    clipboard.on('success', function(e) {
        console.log(e);
    });
    clipboard.on('error', function(e) {
        console.log(e);
    }); 
});