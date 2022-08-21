//document.getElementById("orderForm").onchange = {
//    orderSend(){ document.getElementById("orderForm").submit();
//    document.getElementById("test").innerHTML;}


$(document).on("change", "#order", function (target) {
  let a = $("#order").val()
  document.getElementById("orderForm").submit()

  //window.alert(a);
  //console.log(a);
});

function switchSelected(){
    //var select = document.getElementById('order');
    //var value = select.options[select.selectedIndex].value;
    //value = "rooms"
    //document.getElementById("test").innerHTML = "asdsdas";

    const changeSelected = (e) => {
    const $select = document.querySelector('#order');
    $select.value = 'rooms'
    };
}



//function orderSend(){
//    window.alert("dsadx");
//    document.getElementById("test").innerHTML;
//}
/*
$(document).on("change", "#order", function (target) {

  let a = $("#order");
  $.ajax({
    type: "POST",
    url: "/userFavourites/",
    headers: { "X-CSRFToken": csrftoken },
    data: $("orderForm").serialize(),
    success: function (response) {
      console.log("response")
      console.log(response)
      a.prop("selected", "selected");
     }
  });
});
*/