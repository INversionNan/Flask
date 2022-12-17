$(function (){
    $("#code_btn").click(function (event){
        event.preventDefault();

        var email = $("input[name='email']").val();
        $.ajax({
            url:"/certificationCode/email?email="+email,
            method:"GET",
            success: function (result){
                var code = result['code'];
                if (code === 200){
                    alert("successfully send");
                }
                else{
                    alert(result['message']);
                }
            },
            fail: function(error){
                console.log(error);
            }
        })

    });
});