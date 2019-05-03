var dash=document.getElementById('dashboard');
function open_dash(){
    var dash=document.getElementById('dashboard');
    if (dash.style.display=='block') {
        dash.style.display='none';
    }
    else{
        dash.style.display='block';
        document.getElementById('close').style.display='inline';
    }
}
//closes the dashboard
function close_dash(){
    open_dash();
}

//display the appropriate fa fa-icon when dashboard element is clicked
var x;
function open_dash_elem(x){
    document.getElementsByClassName('main-content')[0].style.display='none';
    if (document.getElementById('dash_'+x)) {
        for (var i=1;i<10;i++)
        {
            document.getElementById('dash_'+i).getElementsByTagName('i')[0].style.display='none';
            //document.getElementsByClassName('hidden-content')[i].style.display='none';
        }
        document.getElementById('dash_'+x).getElementsByTagName('i')[0].style.display='block';


        var page=document.getElementById('dash_'+x);
        if (x==1)
        {
            page.style.display='block';
            document.getElementsByTagName('title').innerHTML='STUDENT D ETAILS';
        }
        if (x==2)
        {
            document.getElementById('classes').style.display='block';
        }
        if (x==3)
        {
            document.getElementById('student-details').style.display='block';
            document.getElementById('full-details').style.display='none';
            document.getElementById('all-students').style.display='block';
        }
        if (x==4)
        {
            page.style.display='block';
        }
        if (x==5)
        {
            page.style.display='block';
        }
        if (x==6)
        {
            page.style.display='block';
        }
        if (x==7)
        {
            page.style.display='block';
        }
        if (x==8)
        {
            page.style.display='block';
        }
    }
}
function close_dash_content(){
    var content=document.getElementById('dashboard');
    if(dash.style.display=='block'){
        dash.style.display='none';
    }
}
//function used to hide default table with marks records
function hide_default_table() {
}

//function to send ajax request to server
function fetch_marks() {
    //document.getElementById('table_marks').style.display='none';
    var xhttp;
    var year=document.getElementById('year').value;
    var clas=document.getElementById('class').value;
    var term=document.getElementById('term').value;
    var subject=document.getElementById('subject').value;
    var id='y='+year+'&c='+clas+'&s='+subject+'&t='+term;
    if (window.XMLHttpRequest) {
        xhttp = new XMLHttpRequest();
    } else {
        // code for IE6, IE5
        xhttp = new ActiveXObject("Microsoft.XMLHTTP");
    }
    xhttp.onreadystatechange = function () {
        if (xhttp.readyState == 4 && xhttp.status == 200) {
            document.getElementById("table_marks").innerHTML = xhttp.responseText;
        }
        else {
            document.getElementById("table_marks").innerHTML='unable to send request';
        }
    };
    xhttp.open("GET", "table_marks.php?" + id, true);
    xhttp.send();
}
/*function to display element used to add new streams*/
var id='';
function add_stream(id){
    var elem=document.getElementById(id);
    elem.style.display='block';
    $("#subjects-table").hide();
    $("#new-subjects").show();
    $("#classes-table").hide();
    $('.edit-subjects').hide();
    $('#delete-subjects-table').hide();

}
/*add new rows to table with streams*/

    $("#add-row").click(function () {
        var name = $("#num-rows").val();
        //var email = $("#email").val();
        for (i = 1; i <= name; i++) {
            var markup = "<tr>" +
                "<td data-title='STREAMS'><input type='text' name='stream[]'></td></tr>";
            $("table tbody").append(markup);
        }
    });

/*add new rows to table with subjects*/

$('#records-add').click(function () {
    var name = $("#num-rows").val();
    //var email = $("#email").val();
    for (i = 1; i <= name; i++) {
        var markup = "<tr>" +
            "<td data-title='SUBJECT CODE'><input type='text'name='subjectCode[]' required></td>" +
            "<td data-title='SUBJECT NAME'><input type='text' name='subjectName[]'></td>" +
            "</tr>";
        $("#new-subject-table tbody").append(markup);
        $('#note').show();
    }
});

/*display edit subjects table*/
$('#edit-button').click(function () {
    $('#subjects-table').hide();
    $('#add-subjects').hide();
    $("#new-subjects").hide();
    $('.edit-subjects').show();
    $('#delete-subjects-table').hide();
});

/*display delete subjects table*/
$('#delete-button').click(function () {
    $('#subjects-table').hide();
    $('.edit-subjects').hide();
    $("#new-subjects").hide();
    $('#add-subjects').hide();
    $('#add-calendar-dates').hide();
    $('#delete-subjects-table').show();
});

/*prompt before deleting*/
$('#delete-subjects').click(function () {
    var flag=confirm('Delete selected subjects');
    if (flag)
        submitNow();
    else
        return false;
});

/*
###################### NEW-MEMBERS.PHP ########################################################*/
var input,feedback;
function validate(input,feedback) {
    var str=$('#'+input+'').val();
    if (input==='fname' || input==='sname' || input==='surname'){
        var regex=/[^a-z]+/gi;
        var flag=regex.test(str);
        if(flag){
            warningIndicator(input);
            $('#'+input+'-err').text(' Name should contain letters only');
        }
        else
        {
            removeWarningIndicator(input,str);
        }
    }
    else if (input==='email'){
        flag=str.indexOf('.');
        var atposition=str.indexOf('@');
        if (flag===-1 || atposition===-1) {
            warningIndicator(input);
            $('#'+input+'-err').text(' invalid email address. it should contain @ and .');

        }
        else {
            removeWarningIndicator(input,str);
        }
    }
    else if (input==='password') {
        length=str.length;
        $('#confirm-err').text('');
        if (length<6){
            warningIndicator(input);
            $('#'+input+'-err').text('password should be at least 6 characters');
        }
        else{
            removeWarningIndicator(input,str);
        }

    }
    else if (input==='confirm'){
        var password=$('#password').val();
        if (password=== null || password===''){
            warningIndicator('password');
            $('#'+input+'-err').show();
            $('#'+input+'-err').text('You must fill the password field fist before filling confirm password');
            $('#password').focus();

        }
    }


}
function warningIndicator(input){
    $('#'+input+'-err').show();
    $('#'+input+'').css('border','1px solid red');
    $('#'+input+'-err').css('color','red');
    $('#'+input+'').focus();
}

function removeWarningIndicator(input,str) {
    $('#'+input+'').css('border','1px');
    $('#'+input+'-err').css('color','green');
    $('#'+input+'-err').text(' entry has been sanitized');
    $('#'+input+'').val(str.toUpperCase());
}

function check_inputs() {
    //$('#submit-new-member').click(function () {
        id = $('#newID').val();
        fname = $('#fname').val();
        sname = $('#sname').val();
        email = $('#email').val();
        if (id === '' || id == null) {
            $('#newID').focus();
            $('#newID-err').show();
            $('#newID-err').text('this field must be filled');
            return false;
        }
        if (fname==='' || fname===null){
            $('#fname').focus();
            $('#fname-err').show();
            $('#fname-err').text('this field must be filled');
            return false;
        }
        submitNow();
  //  });
}
/*script for adding new term dates*/
$('#no-of-dates').click(function () {
    var name = $("#num-rows").val();
    //var email = $("#email").val();
    for (i = 1; i <= name; i++) {
        var markup = "<tr>" +
            "<td data-title='Year'><input type='text'name='year[]' required></td>" +
            "<td data-title='Term'><input type='text' name='term[]' required></td>" +
            "<td data-title='Opening Date'><input type='date' name='openingDate[]' required></td>" +
            "<td data-title='Closing Date'><input type='date' name='closingDate[]' required></td>" +
            "</tr>";
        $("#new-subject-table tbody").append(markup);
    }
});