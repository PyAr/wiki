/** 
 * Just a small script to redirect to http://www.staging.python.org.ar/
 * when using the staging environment
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
