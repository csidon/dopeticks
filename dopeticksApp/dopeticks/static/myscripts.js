function revealFunction() {
  var todo = document.getElementById("todo-section");
  var progress = document.getElementById("progress-section");
  var done = document.getElementById("done-section");
  var overdue = document.getElementById("overdue-section");
  if (todo.style.display === "none") {
    todo.style.display = "block";
    progress.style.display = "none";
    done.style.display = "none";
    overdue.style.display = "none";
  } else {
    todo.style.display = "none";
  }
  alert("to do clicked");
}

