/**
 * User: Den Schigrov <dennytwix@gmail.com>
 * Created: 26.02.13
 *
 * Id: $Id$
 */
$(document).ready(function() {
    $('a[href$="send_email/"]').click(function(){
         var msg = $.msgBox({ type: "prompt",
            title: "Please enter lawyers email",
            inputs: [
                { header: "Email", type: 'text', name: "email" }
                ],
            buttons: [
                { value: "Send" }, {value:"Cancel"}],
            success: function (result, values) {
                if (result == "Cancel"){

                }else{
                    var email = "";
                    $(values).each(function (index, input) {
                        if (input.name == "email"){
                            email = input.value;
                        }
                    });
                    $.ajax({
                        url: 'send_email/',
                        type: "GET",
                        data: {
                            email: email
                        },
                        complete: function(data){

                        }
                    });
                }

//                $.post('send_email/', {
//                    email: email
//                }, onAjaxSuccess);
//                function onAjaxSuccess(data)
//                {
//                    // Здесь мы получаем данные, отправленные сервером и выводим их на экран.
//                    alert(data);
//                }
            }
        });
        return false;
    });
});
