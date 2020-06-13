$('document').ready(function(){
  $('#dselect').change(function()
  {
    var dval = $('#dselect').val()
    // console.log(dval)
    // console.log(dval)
    if(dval==='name')
    {
      $( function()
      {
        var availableTags = [
          "Shashish",
          "Rohini",
          "Rohit",
          "Shyam",
          "sita",
          "Radha",
          "Ramesh",
          "Radh"
        ];
        $( "#tags" ).autocomplete({
          source: availableTags
        });
      });
    }
    else if (dval==='pan')
    {
      $( function()
      {
        var availableTags = [
          "POIUH1256932569",
          "96352QWERT89652",
          "123456789",
          "789456132",
          "789456132",
          "ABCDE1324513245",
          "PLOIJ36589QWERT",
          "R9R6R6R3R2R1RR1"
        ];
        $( "#tags" ).autocomplete({
          source: availableTags
        });
      });
    }
    else if (dval==='age')
    {
      $( function()
      {
        var availableTags = ["18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50" ];
        $( "#tags" ).autocomplete({
          source: availableTags
        });
      });
    }
    else if (dval==='gender')
    {
      $( function()
      {
        var availableTags = [
          "Male",
          "Female"
        ];
        $( "#tags" ).autocomplete({
          source: availableTags
        });
      });
    }
    else if (dval==='email')
    {
      $( function()
      {
        var availableTags = [
          "shash@gmail.com",
          "rohini@gmail.com",
          "rohit@gmail.com",
          "shyam@gmail.com"
        ];
        $( "#tags" ).autocomplete({
          source: availableTags
        });
      });
    }
    else if (dval==='city')
    {
      $( function()
      {
        var availableTags = ["Ram",
          "govidpuri",
          "Nagpur",
          "Chitrakoot",
          "Lucknow",
          "Kanpur",
          "Mathura",
          "Rampur"
        ];
        $( "#tags" ).autocomplete({
          source: availableTags
        });
      });
    }
    else
    {
      alert('Sorry')
    }
    // alert($('#dselect').val())
  });
});
