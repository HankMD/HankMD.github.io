// Function for loading content into the template
function loadTemplate() {
  $("#template").load("/template.html", function() {
    $("#content").appendTo("#content-container");
  });
}

// Function for setting navbar pills to active
function setActive(id) {
  waitForElement(id, () => {$(id).addClass("active");})
}

// Runs the callback when the selector exists
function waitForElement(selector, callback) {
  if ($(selector).length) {
    callback();
  } else {
    setTimeout(function() {
      waitForElement(selector, callback);
    }, 1);
  }
};
