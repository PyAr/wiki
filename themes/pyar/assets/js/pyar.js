/** 
 * Just a small script to redirect to http://www.staging.python.org.ar/
 * when using the staging environment, and to correct the link that is
 * active
 */
if (window.location.host.includes("staging")) {
    $(".nav-link").each(function(index) {
        var href = $(this).attr("href");
        if (href.includes("python.org.ar")) {
            href = href.replace("python.org.ar", "staging.python.org.ar");
            $(this).attr("href", href);
        }
    });
}


$(".nav-item").removeClass("active");
var pathname = window.location.pathname;
var headerElement = $(".wiki");
if (pathname == "/pyar/") {
    headerElement = $(".quienes_somos");
} else if (pathname == "/listadecorreo/" || pathname == "/foro_y_redes/") {
    headerElement = $(".navbar_lista_de_correo");
} else if (window.location.host.includes("planeta")) {
    headerElement = $(".pyar")
} 
headerElement.parent().parent().addClass("active");
