document.getElementById("searchBar").addEventListener("keyup", function(event) {
    // Number 13 is the "Enter" key on the keyboard
    if (event.keyCode == 13) {
    // Cancel the default action, if needed
    event.preventDefault();
    // Trigger the button element with a click
    document.getElementById("btnSearch").click();
    }
});
var counter = 0;

function empty(id){
    id.value = "";
}

function populate(){
    counter = 0;
    let params = document.getElementById("searchBar").value;
    $.ajax({
        type:"POST",
        url:"/perform_search",
        data: params,
        dataType:"json",
        success:function(patients){
            for( var person in patients){
                person["name"]
                $('#searchResults').append('<a>href="/patient/'+person["tel"]+'"</a></br></br>');
            }
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            alert("Request: " + XMLHttpRequest.toString() + "\nStatus: " + textStatus + "\nError: " + errorThrown);
        },
    });
}

function collect_data(){
    for(let i=0; i <= counter; i++){
        document.getElementById(i.toString()).value;
    }
}
function submit(){
    let collected = collect_data()
    $.ajax({
       type:"POST",
       url:"/update_db",
       data:collected,

    });
}