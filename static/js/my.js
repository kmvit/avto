$(document).ready(function() {
    
    $('button#yes').on("click", function(event) {
        var name = $("button#yes").val();
        $.cookie('pst',name,{
            path: '/',
        });
        $('#close, #overlay_city').click();
        location.reload();
        });
    

    
    $('button#no').on("click", function(event) {

        $('#close, #overlay_city').click();
        $('#overlay').fadeIn(400,
            function() {
                $('#modal_form1')
                    .css('display', 'block')
                    .animate({
                        opacity: 1,
                        top: '50%'
                    }, 200);
            });
        
        $('#modal_form1')
            .animate({
                    opacity: 0,
                    top: '45%'
                }, 200,
                function() {
                    $(this).css('display', 'none');
                    $('#overlay').fadeOut(400);
                }
            );
    });
    $('.location-name').click(function(e) {
        var q = $(".location-name").text();
        $.removeCookie('pst', q);
        $('#overlay').fadeIn(400,
            function() {
                $('#modal_form1')
                    .css('display', 'block')
                    .animate({
                        opacity: 1,
                        top: '50%'
                    }, 200);
            });

    });
    $('#sub').on("click", function() {
        var cuck = $('#id_school_town').val();
        $.cookie('pst', cuck, {
            path: '/',
        });
        $.cookie('rel', 1, {
            path: '/',
        });
     

    });
    

});
    $(function() {
        // Проверяем запись в куках о посещении
        // Если запись есть - ничего не происходит
         if (!$.cookie('pst')) {
        // если cookie не установлено появится окно
        // с задержкой 5 секунд
        var delay_popup = 5000;
        setTimeout("document.getElementById('overlay_city').style.display='block'", delay_popup);
         }
    });

    $(document).ready(function() {
        if ($.cookie('noShowWelcome')) $('.policity-private').hide();
        else {
            $("#close-welcome").click(function() {
                $(".policity-private").fadeOut(1000);
                $.cookie('noShowWelcome', true,{
            path: '/',
        });    
            });
        }
    });

    $(document).ready(function(){

    $("#back-top").hide();
    $(function () {
        $(window).scroll(function () {
            if ($(this).scrollTop() > 100) {
                $('#back-top').fadeIn();
            } else {
                $('#back-top').fadeOut();
            }
        });

        $('#back-top a').click(function () {
            $('body,html').animate({
                scrollTop: 0
            }, 800);
            return false;
        });
    });

});
