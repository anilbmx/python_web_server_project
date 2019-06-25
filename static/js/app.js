// $(document).ready(function() {
function TranslateApi(event) {
  event.preventDefault();
  $("#submit").attr("disabled", true);
  var input_txt = $("#ttext").val().trim();
  $.ajax({
        data : {
           inptxt : input_txt
               },
           type : 'POST',
           url : window.location.origin+"/translate"
          })
      .done(function(idata) {
        $("#optxt").val(idata['output']);
        $("#submit").attr("disabled", false);
      })
      .fail(function() {
        alert( "error" );
        $("#submit").attr("disabled", false);
      })
}

function employees_detls(event){
  event.preventDefault();
  $.get(window.location.origin+"/get_employee_data",function(data){
    console.log(data['output']);
    // console.log(JSON.parse(data['output']));
    $("#eoutput").html(data['output'])
  })
}
