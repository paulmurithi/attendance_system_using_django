$(document).ready(function () {
    $('.filter').on('submit', function (event) {
       event.preventDefault();
       let id_no = $('#id_adm_no').val();
       let unit_code = $('#id_unit_code').val();
       let course_code = $('#id_course_code').val();
       console.log(id_no, unit_code, course_code)

    });

});