function myFunction() {
  var x = document.getElementById("todo-section");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
  alert("js connection check");
}