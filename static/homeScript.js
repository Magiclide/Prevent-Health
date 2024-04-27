  // Get the element with the id "arrow1"
  var arrow1 = document.getElementById('arrow1');
  var arrow2 = document.getElementById('arrow2');
  var arrow3 = document.getElementById('arrow3');
  var arrow4 = document.getElementById('arrow4');
  var additionalText1 = document.getElementById('additionalText1'); 
  var additionalText2 = document.getElementById('additionalText2');
  var additionalText3 = document.getElementById('additionalText3');
  var additionalText4 = document.getElementById('additionalText4'); 
  var backgroundFrequentQuestions = document.getElementById('frequent-questions');
  var rectangle2 = document.getElementById('rectangle2');
  var rectangle1 = document.getElementById('rectangle1');


  var isAdditionalTextOneVisible=false;
  var isAdditionalTextTwoVisible=false;
  var isAdditionalTextThreeVisible=false;
  var isAdditionalTextFourVisible=false;

   
  arrow1.addEventListener('click', function() {
    arrow1.classList.toggle('rotate');
    additionalText1.classList.toggle('hidden');
   
    if(!isAdditionalTextTwoVisible && !isAdditionalTextThreeVisible && !isAdditionalTextFourVisible) backgroundFrequentQuestions.classList.toggle('expandBackground')
      isAdditionalTextOneVisible=!isAdditionalTextOneVisible
      
  });
  arrow2.addEventListener('click', function() {
  
    arrow2.classList.toggle('rotate');
    additionalText2.classList.toggle('hidden')
    


    if(!isAdditionalTextOneVisible && !isAdditionalTextThreeVisible && !isAdditionalTextFourVisible) backgroundFrequentQuestions.classList.toggle('expandBackground')
    isAdditionalTextTwoVisible=!isAdditionalTextTwoVisible
    
  });
  arrow3.addEventListener('click', function() {
    this.classList.toggle('rotate');
    additionalText3.classList.toggle('hidden')
    
    if(!isAdditionalTextTwoVisible && !isAdditionalTextOneVisible && !isAdditionalTextFourVisible) backgroundFrequentQuestions.classList.toggle('expandBackground')
    isAdditionalTextThreeVisible=!isAdditionalTextThreeVisible
    
  });
  arrow4.addEventListener('click', function() {
   
    this.classList.toggle('rotate');
    additionalText4.classList.toggle('hidden')
    
    if(!isAdditionalTextTwoVisible && !isAdditionalTextThreeVisible && !isAdditionalTextOneVisible) backgroundFrequentQuestions.classList.toggle('expandBackground')
    isAdditionalTextFourVisible=!isAdditionalTextFourVisible
  });
  function myFunction(x) {
    x.classList.toggle("change");
    
      var sidebar = document.getElementById('sidebar');
    
      sidebar.style.display= (sidebar.style.display==='none') ? 'none' : 'block';
      sidebar.style.left = (sidebar.style.left === '' || sidebar.style.left === '-100%') ? '0' : '-100%';
    
  }
  document.addEventListener("DOMContentLoaded", function () {
    var modelosLink = document.getElementById("modelosLink");
    var arrowIcon = document.getElementById("arrowIcon");
    var submenu = document.querySelector("#menu .submenu");

    modelosLink.addEventListener("click", function () {
        submenu.classList.toggle("visible");
    });
});