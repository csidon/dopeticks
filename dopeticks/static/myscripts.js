$(document).ready(function() {
    $('#todo-section, #progress-section, #done-section, #overdue-section, #archived-section').hide();

    $('#cardtodo').click(function() {
        $('.cardTag').not(this).removeClass('card-bigger');
        $('.btn-outline-info').not(this).removeClass('active');
        $(this).toggleClass('card-bigger');
        $('#todo-section').show();
        $('#default-section').hide();
        $('#progress-section').hide();
        $('#done-section').hide();
        $('#overdue-section').hide();
        $('#archived-section').hide();
    });

    $('#carddoing').click(function() {
        $('.cardTag').not(this).removeClass('card-bigger');
        $('.btn-outline-info').not(this).removeClass('active');
        $(this).toggleClass('card-bigger');
        $('#todo-section').hide();
        $('#default-section').hide();
        $('#progress-section').show();
        $('#done-section').hide();
        $('#overdue-section').hide();
        $('#archived-section').hide();
    });

    $('#carddone').click(function() {
        $('.cardTag').not(this).removeClass('card-bigger');
        $('.btn-outline-info').not(this).removeClass('active');
        $(this).toggleClass('card-bigger');
        $('#todo-section').hide();
        $('#default-section').hide();
        $('#progress-section').hide();
        $('#done-section').show();
        $('#overdue-section').hide();
        $('#archived-section').hide();
    });

    $('#cardoverdue').click(function() {
        $('.cardTag').not(this).removeClass('card-bigger');
        $('.btn-outline-info').not(this).removeClass('active');
        $(this).toggleClass('card-bigger');
        $('#todo-section').hide();
        $('#default-section').hide();
        $('#progress-section').hide();
        $('#done-section').hide();
        $('#overdue-section').show();
        $('#archived-section').hide();
    });

    $('#archived-btn').click(function() {
        $('.cardTag').not(this).removeClass('card-bigger');
        $('.btn-outline-info').not(this).removeClass('active');
        $(this).toggleClass('active');
        $('#todo-section').hide();
        $('#default-section').hide();
        $('#progress-section').hide();
        $('#done-section').hide();
        $('#overdue-section').hide();
        $('#archived-section').show();
    });
  
});



    // $('#todo-section, #progress-section, #done-section, #overdue-section, #archived-section').hide();
    // function revealFunction(id) {
    //   $('#' + id).show();
    //   btn.classList.toggle('highlight');

//       var defaults = document.getElementById("default-section");
//       var todo = document.getElementById("todo-section");
//       var progress = document.getElementById("progress-section");
//       var done = document.getElementById("done-section");
//       var overdue = document.getElementById("overdue-section");
//       var archived = document.getElementById("archived-section");

//     //  const button1 = document.getElementById('todo-btn');
//     //  const button2 = document.getElementById('doing-btn');
//     //  const button3 = document.getElementById('done-btn');
//     //  const button4 = document.getElementById('overdue-btn');

//         document.getElementById(id).style.display = 'block';
//         // hide the lorem ipsum text
//         if (btn == "defaults"){
//             progress.style.display = 'none';
//             todo.style.display = 'none';
//             done.style.display = 'none';
//             overdue.style.display = 'none';
//             archived.style.display = 'none';
//         }

//         if (btn == "todo"){
//             $('todo-section').show();
//             defaults.style.display = 'none';
//             progress.style.display = 'none';
//             done.style.display = 'none';
//             overdue.style.display = 'none';
//             archived.style.display = 'none';
//         }
//         else if (btn == "done"){
//             defaults.style.display = 'none';
//             progress.style.display = 'none';
//             todo.style.display = 'none';
//             overdue.style.display = 'none';
//             archived.style.display = 'none';
//         }
//         else if (btn == "progress"){
//             defaults.style.display = 'none';
//             todo.style.display = 'none';
//             done.style.display = 'none';
//             overdue.style.display = 'none';
//             archived.style.display = 'none';
//         }
//         else if (btn == "overdue"){
//             defaults.style.display = 'none';
//             progress.style.display = 'none';
//             done.style.display = 'none';
//             todo.style.display = 'none';
//             archived.style.display = 'none';
//         }
//         else if (btn == "archived"){
//             defaults.style.display = 'none';
//             progress.style.display = 'none';
//             done.style.display = 'none';
//             todo.style.display = 'none';
//             overdue.style.display = 'none';
//         }
//         else{
//         console.log("smth else is clicked")
//         }

//     }
// });
