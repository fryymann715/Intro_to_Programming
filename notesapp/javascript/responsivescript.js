    function openDesc(element_id) {
        var ele = document.getElementById(element_id);
            var mainele = ele.querySelectorAll("main");
        var eleTitle = ele.querySelectorAll("header");
        var cview = document.getElementById("current-concept");
        var cVtitle = document.getElementById("current-concept-title");
        var cdesc = mainele[0].innerHTML;
        var ctitle = eleTitle[0].innerHTML;

        cview.innerHTML = cdesc;
        cVtitle.innerHTML = ctitle;

    }