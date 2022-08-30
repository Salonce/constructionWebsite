$(document).on("change", "#order", function (target) {
  //let a = $("#order").val()
  document.getElementById("orderForm").submit()
});


$(document).on("click", ".fav", function (target) {

    let idVariable = target.target.id;
    console.log("houseplan id: ", target.target.id);
    console.log("csrftoken: ", csrftoken);

    $.ajax({
         url: '',
         headers: {
            'X-CSRFToken': csrftoken,
            'Content-Type': 'application/json'
            //'X-Requested-With': 'XMLHttpRequest',
         },
         mode: 'same-origin',
         type: 'post',
         data: {
            'housePlanID': 'czcxz',
         },
         success: function(response) {
            console.log("i am inside post request, success")
            //$(".btn").text(response.bbb)
            //$("#helper").text("<div>dsadsa</div><div>dsacxvzxcvx</div>")
            //$("#helper").text(response[0].fields.house_plan)
         },
         error: function(response) {
            console.log("i am inside post request, failure")
            //alert("Something didn't work out!!");
            //$(".btn").text("error")
         }
    });
});



//get order value into a variable??
/*
$(document).on("change", "#order", function (target) {
  let order_value = $("#order").val()
*/

  //$("#helper").text(order_value)
/*
  $.ajax({
         url: '',
         headers: {
            //'X-Requested-With': 'XMLHttpRequest',
            'Content-Type': 'application/json'
         },
         type: 'get',
         data: {
            someText: order_value
         },
         success: function(response) {
            //$(".btn").text(response.bbb)
            $("#helper").text("<div>dsadsa</div><div>dsacxvzxcvx</div>")
            //$("#helper").text(response[0].fields.house_plan)
         },
         error: function(response) {
            //alert("Something didn't work out!!");
            //$(".btn").text("error")
         }
      });
});

*/
/*
$(document).ready(function(){
   $(".btn").click(function(){
      $.ajax({
         url: 'loadInfo/',
         headers: {
            //'X-Requested-With': 'XMLHttpRequest',
            'Content-Type': 'application/json'
         },
         type: 'get',
         data: {
            someText: 'somtaaaaaaaaaaaaaaaaaaaaaaaaa'
         },
         success: function(response) {
            //$(".btn").text(response.seconds)
            $(".btn").text(response.tree)
            console.log(response)
         },
         error: function(response) {
            alert("Something didn't work out!!");
            $(".btn").text("error")
         }
      });
   });
});
*/


/*
var tag = document.createElement("p");
var text = document.createTextNode("Tutorix is the best e-learning platform");
tag.appendChild(text);
var element = document.getElementById("new");
element.appendChild(tag);
*/




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