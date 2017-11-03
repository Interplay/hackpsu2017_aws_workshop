$(document).ready(function() {
    $('#checkin').modal({dismissible: true});
    $('#s3st1').modal({dismissible: true});
    $('#s3st2').modal({dismissible: true});
    $('#s3st3').modal({dismissible: true});
    $('#s3st4').modal({dismissible: true});
    $('#ec2st1').modal({dismissible: true});
    $('#ec2st2').modal({dismissible: true});
    $('#ec2st3').modal({dismissible: true});
    $('#ec2st4').modal({dismissible: true});
    $('#ec2st5').modal({dismissible: true});
    $('#ec2st6').modal({dismissible: true});
    $('#ec2st7').modal({dismissible: true});
    $('#ec2st8').modal({dismissible: true});
    $('#ec2st9').modal({dismissible: true});
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