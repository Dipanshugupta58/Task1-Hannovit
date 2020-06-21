$(function(){

  $(".container").css("display","none");
  $(".container").fadeIn(1000);


  // $("#fRecord legend").on("click",function(){
  // $(".table").stop().slideUp(3000);
  // });

  $("#fRecord legend").on("click",function(){
    $(".table").stop().slideToggle(1000);
  });

  $("#fRecord legend").hover(function(){
    $(this).css("color","red");
    $(this).text("Click Me") ;
  },function(){
    $(this).css("color","Black");
    $(this).text("Record");
  });

});
