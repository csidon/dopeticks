//function revealFunction(id, btn) {
//  var todo = document.getElementById("todo-section");
//  var progress = document.getElementById("progress-section");
//  var done = document.getElementById("done-section");
//  var overdue = document.getElementById("overdue-section");
//  var archived = document.getElementById("archived-section");
//
////  const button1 = document.getElementById('todo-btn');
////  const button2 = document.getElementById('doing-btn');
////  const button3 = document.getElementById('done-btn');
////  const button4 = document.getElementById('overdue-btn');
//
//    document.getElementById(id).style.display = 'block';
//    // hide the lorem ipsum text
//    if (btn == "todo"){
//        progress.style.display = 'none';
//        done.style.display = 'none';
//        overdue.style.display = 'none';
//        archived.style.display = 'none';
//        var card = document.getElementById("todo-btn");
//        document.getElementById("todo-btn").classList.toggle("card-bigger");
//        document.getElementById("done-btn").classList.remove("card-bigger");
//        document.getElementById("doing-btn").classList.remove("card-bigger");
//        document.getElementById("overdue-btn").classList.remove("card-bigger");
//
//    }
//    else if (btn == "done"){
//        progress.style.display = 'none';
//        todo.style.display = 'none';
//        overdue.style.display = 'none';
//        archived.style.display = 'none';
//        var card = document.getElementById("done-btn");
//        card.classList.toggle("card-bigger");
//        document.getElementById("todo-btn").classList.toggle("card-bigger");
//        document.getElementById("done-btn").classList.remove("card-bigger")
//        document.getElementById("doing-btn").classList.remove("card-bigger")
//        document.getElementById("overdue-btn").classList.remove("card-bigger")
//    }
//    else if (btn == "progress"){
//        todo.style.display = 'none';
//        done.style.display = 'none';
//        overdue.style.display = 'none';
//        archived.style.display = 'none';
//        var card = document.getElementById("doing-btn");
//        card.classList.toggle("card-bigger");
//    }
//    else if (btn == "overdue"){
//        progress.style.display = 'none';
//        done.style.display = 'none';
//        todo.style.display = 'none';
//        archived.style.display = 'none';
//        var card = document.getElementById("overdue-btn");
//        card.classList.toggle("card-bigger");
//    }
//    else if (btn == "archived"){
//        progress.style.display = 'none';
//        done.style.display = 'none';
//        todo.style.display = 'none';
//        overdue.style.display = 'none';
//    }
//    else{
//    console.log("smth else is clicked")
//    }
//
//}
//
