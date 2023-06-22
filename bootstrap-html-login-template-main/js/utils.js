function addTar(data, index) {
            var permiss = localStorage.getItem("permission")
            var th = $("<th>", {
                "scpoe": "row",
                "html": index
            })
            if(permiss == "admin") {
                th.html("")
                th.append($("<input>", {
                    "type": "checkbox"
                }))
            }
            var tar = $("<tr>").append(
                $("<td>", {
                    "html": data.name
                }),
                $("<td>", {
                    "html": data.sex
                }),
                $("<td>", {
                    "html": data.tel
                }),
                $("<td>", {
                    "html": data.address
                }),
                $("<td>", {
                    "html": data.birth
                }),
                $("<td>", {
                    "html": data.academy
                }),
                $("<td>", {
                    "html": data.specialize
                })
            )
            tar.prepend(th)
            return tar
        }
function retainReq(url) {
        var params = new Object();
        if ( url.indexOf( "?" ) != -1 ) {
            var str = url.substr(1); //substr()方法返回从参数值开始到结束的字符串；
            var strs = str.split("&");
            for (var i = 0; i < strs.length; i++) {
                params[strs[i].split("=")[0]] = (strs[i].split("=")[1]);
            }
        }
        return params
}