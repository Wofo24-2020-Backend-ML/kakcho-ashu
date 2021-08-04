console.log(22+3)


function SubmitData() {
    var file = document.getElementById("inpFile").files[0];
    var column_name = document.getElementById("column_name").value;
    var form = new FormData();

    form.append("file", file);
    form.append("column_name", column_name);

    var settings = {
      "async": true,
      "crossDomain": true,
      "url": "https://kakcho-ashu.herokuapp.com/csvupload/task2/",
      "method": "POST",
      "headers": {
      "cache-control": "no-cache"
    },
    
    "processData": false,
    "contentType": false,
    "mimeType": "multipart/form-data",
    "data": form
    }

    $.ajax(settings).done(function SubmitData(response) {
      console.log(response)}
    );
};