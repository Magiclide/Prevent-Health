$(document).ready(function () {
  var formSteps = $(".input-field");
  var currentStep = 0;

  function showCurrentStep() {
    formSteps.hide();
    formSteps.eq(currentStep).show();
  }

  showCurrentStep();

  // Listen for the "keydown" event on input and select elements
  formSteps.on("keydown", function (e) {
    // Check if the "Tab" key (key code 9) was pressed
    if (e.keyCode === 9) {
      e.preventDefault();

      // Validate the current step before proceeding
      var currentInput = formSteps.eq(currentStep);
      if (currentInput[0].checkValidity()) { // Use [0] to access the DOM element
        currentStep++;
        if (currentStep < formSteps.length) {
          showCurrentStep();
        } else {
          // All steps completed, you can submit the form here
          $("#formulario").submit();
        }
      }
    }
  });

  // Add a click event listener to the document to prevent hiding when clicking outside
  $(document).on("click", function (e) {
    var clickedElement = $(e.target);
    if (!clickedElement.is(".input-field, .input-field *")) {
      // Instead of hiding elements, set their visibility to "visible"
      formSteps.eq(currentStep).css("visibility", "visible");
    }
  });
});
  
  
  
  
  