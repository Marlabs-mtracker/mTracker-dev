$(document).ready(function () {
    $('.collapsible').collapsible();
});

// date-time picker 
$(document).ready(function () {
    $('.datepicker').datetimepicker({
        minDate: new Date(),
        format: 'm/d/Y, h:i:s A'
    });
});

$('#task-update-btn').on('click', function(){
    window.location.href = "../update-task.html";
})