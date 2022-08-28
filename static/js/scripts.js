
$(document).on("change", "#order", function (target) {
  //let a = $("#order").val()
  document.getElementById("orderForm").submit()

  //window.alert(a);
  //console.log(a);
});


$(document).ready(function(){
   $(".btn").click(function(){
      $.ajax({
         url: 'loadInfo/',
         headers: {
            'X-Requested-With': 'XMLHTtpRequest',
            'Content-Type': 'application/json'
         },
         type: 'get',
         data: {
            someText: 'somtaaaaaaaaaaaaaaaaaaaaaaaaa'
         },
         success: function(response) {
            //$(".btn").text(response.seconds)
            $(".btn").text(response.bbb)
         },
         error: function(response) {
            alert("Something didn't work out!!");
            $(".btn").text("error")
         }
      });
   });

});

/*
document.getElementById("orderForm").onchange = {
   orderSend(){ document.getElementById("orderForm").submit();
    document.getElementById("test").innerHTML;}

function orderSend(){
   window.alert("dsadx");
   document.getElementById("test").innerHTML;
}

$(document).on("change", "#order", function (target) {
*/