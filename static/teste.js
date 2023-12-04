$(document).ready(function () {
    var formSteps = $(".form-step");
    var currentStep = 0;
    const navDots = document.querySelectorAll('.nav-dot');
    
    function showCurrentStep() {
        formSteps.removeClass("active");
        formSteps.eq(currentStep).addClass("active");
       
        //formSteps.not(".active").find("input, select").prop("disabled", true);
        formSteps.eq(currentStep).find("input, select").prop("disabled", false);
        
        navDots.forEach((dot, index) => {
            const attIndex=index-1;
            if (attIndex === currentStep) {
                dot.classList.add('active-dot');
            } else {
                dot.classList.remove('active-dot');
            }
        });
    }

    showCurrentStep();
    
    $("#next-button").on("click", function (e) {
        e.preventDefault();
        if (currentStep < formSteps.length - 1) {
            var currentInput = formSteps.eq(currentStep).find("input, select");
            if (currentInput[0].checkValidity()) {
                currentStep++;
                showCurrentStep();
            }
        } else {
            
            $("#formulario").submit();
               
            
        }
    });
/*
    var form = $("#formulario");

   form.on("submit", function(event) {
        event.preventDefault();

        var formElements = form.find("input, select");

        var allFieldsFilled = true;

        formElements.each(function() {
            var element = $(this);

            if (element.prop("required") && element.val().trim() === "") {
                allFieldsFilled = false;
                return false; // You can use return false to break out of the loop early
            }
        });

        if (allFieldsFilled) {
            $("#formulario").submit();
        } else {
            console.log("erro");
        }
    });
*/
    
    navDots.forEach((navDot, index) => {
        
        navDot.addEventListener('click', () => {
            const adjustedIndex = index - 1;
            if (adjustedIndex < formSteps.length) {
                currentStep = adjustedIndex;
                showCurrentStep();
            }
        });
    });

    $(document).on("keydown", function (e) {
        if (e.which === 9) {
            e.preventDefault();
            if (currentStep < formSteps.length - 1) {
                var currentInput = formSteps.eq(currentStep).find("input, select");
                if (currentInput[0].checkValidity()) {
                    currentStep++;
                    showCurrentStep();
                }
            } else {
                
               
                
                
            }
        }
    });
    
});
