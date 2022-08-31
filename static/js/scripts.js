$(document).on("change", "#order", function (target) {
  //let a = $("#order").val()
  document.getElementById("orderForm").submit()
});

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

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
         data: JSON.stringify({ "housePlanID": idVariable}),
         success: function(response) {
            console.log("i am inside post request, success")
            if(response.state=="deleted"){
                console.log(response.state);
                $(target.target).removeClass("fav-activated");
                console.log(target);
                //deactivate class selected
            }
            else if(response.state=="added"){
                $(target.target).addClass("fav-activated");
                console.log(response.state)
            }
                //activate class selected
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