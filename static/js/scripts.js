var getUrlParameter = function getUrlParameter(sParam) {
    var sPageURL = window.location.search.substring(1),
        sURLVariables = sPageURL.split('&'),
        sParameterName,
        i;

    for (i = 0; i < sURLVariables.length; i++) {
        sParameterName = sURLVariables[i].split('=');

        if (sParameterName[0] === sParam) {
            return sParameterName[1] === undefined ? true : decodeURIComponent(sParameterName[1]);
        }
    }
    return false;
};

$(document).ready(function(){
    var sortparam = getUrlParameter('sort');
        if (sortparam != 'name' && sortparam != 'total_area' && sortparam != 'price' && sortparam != 'rooms'){
            sortparam = 'name'
        }
        $("#sort").val(sortparam).change();
    console.log("whaaa");

    // (GET FORM) SUBMIT SORT CHANGE
    $(document).on("change", "#sort", function (target) {
        document.getElementById("sortForm").submit();
    });
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


$(document).ready(function(){
    /* loca = console.log(top.location.pathname) */
    if (top.location.pathname === '/housePlanBrowser/'){
            console.log(document);
            console.log(top)
        }


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
                    $(target.target).removeClass("fav-activated");
                }
                else if(response.state=="added"){
                    $(target.target).addClass("fav-activated");
                }
             },
             error: function(response) {
                console.log("i am inside post request, failure")
             }
        });
    });
});



