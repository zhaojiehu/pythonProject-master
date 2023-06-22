$(function (){
        $("#selectAll").on("click", (e) => {
            $("#inputUsername").val("")
            $("#inputAddress").val("")
            $("#inputSpecialize").val("")
            $("tbody").children().remove()
            $.ajax({
            method: "get",
            url: "http://localhost/main/",
            async: true,
            success: (res) => {
                res = JSON.parse(res)
                if(res.status== 200) {
                    for(var i = 0; i < res.data.length; i++ ) {
                        $("tbody").append(addTar(res.data[i]))
                    }
                }
            }
        })
        })
        // 根据用户名查询
        $("#selectUsername").on("click", (e) => {
            var keywords= $("#inputUsername").val()
            if(keywords == '') return;
            $("#inputAddress").val("")
            $("#inputSpecialize").val("")
            $.ajax({
                method: "get",
                url: "http://localhost/select/name/",
                data: {
                    "keywords": keywords
                },
                success: (res) => {
                    res = JSON.parse(res)
                    if(res.status == 200) {
                        $("tbody").empty()
                        for(var i = 0; i < res.data.length; i++ ) {
                            $("tbody").append(addTar(res.data[i]))
                        }
                    }
                }
            })
        })
        // 根据地区查询
        $("#selectAddress").on("click", (e) => {
            var keywords= $("#inputAddress").val()
            if(keywords == '') return;
            $("#inputUsername").val("")
            $("#inputSpecialize").val("")
            $.ajax({
                method: "get",
                url: "http://localhost/select/address/",
                data: {
                    "keywords": keywords
                },
                success: (res) => {
                    res = JSON.parse(res)
                    console.log(res)
                    if(res.status == 200) {
                        $("tbody").empty()
                        for(var i = 0; i < res.data.length; i++ ) {
                            $("tbody").append(addTar(res.data[i]))
                        }
                    }
                }
            })
        })
         // 根据专业查询
        $("#selectSpecialize").on("click", (e) => {
            var keywords= $("#inputSpecialize").val()
            if(keywords == '') return;
            $("#inputAddress").val("")
            $("#inputUsername").val("")
            $.ajax({
                method: "get",
                url: "http://localhost/select/specialize/",
                data: {
                    "keywords": keywords
                },
                success: (res) => {
                    res = JSON.parse(res)
                    console.log(res)
                    if(res.status == 200) {
                        $("tbody").empty()
                        for(var i = 0; i < res.data.length; i++ ) {
                            $("tbody").append(addTar(res.data[i]))
                        }
                    }
                }
            })
        })
        $("#layout").on("click", (e) => {
            localStorage.removeItem("userName")
            localStorage.removeItem("passWord")
            localStorage.removeItem("check2")
            localStorage.removeItem("check1")
            localStorage.removeItem('permission')
            location = "login.html"
        })

        $("#addContact").on('click', function () {
            location.href = "add.html"
        })

        $("#updateContact").on('click', function () {
            const els = $("tbody").children().children("th").children("input")
            let name = ""
            for(var i = 0; i < els.length; i++) {
                if($(els[i]).prop("checked")) {
                    name = $("tbody").children().eq(i).children().eq(1).html()
                    break;
                }
            }
            if(name) {
                location.href = 'update.html?name=' + name
            }else {
                confirm("请勾选你要选择修改的学生！")
            }
        })
        $("#delContact").on('click', function () {
            const els = $("tbody").children().children("th").children("input")
            let array = []
            for(var i = 0; i < els.length; i++) {
                if($(els[i]).prop("checked")) {
                    const name = $("tbody").children().eq(i).children().eq(1).html()
                    array.push(name)
                }
            }
            if(array.length) {
                if(confirm("你确定要删除吗？")) {
                    let delData = {
                        "data": array
                    }
                    delData = JSON.stringify(delData)
                    $.ajax({
                        method: "post",
                        url: "http://127.0.0.1/delcontact/",
                        data: delData,
                        success: (res) => {
                            var res = JSON.parse(res)
                            const {status, msg, data} = res
                            if(status == 200) {
                                $("#selectAll").click()
                            }
                        }
                    })
                }
            }
            else {
                confirm("请勾选你要删除的学生！")
            }
        })
})