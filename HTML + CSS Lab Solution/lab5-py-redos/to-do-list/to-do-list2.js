//     let button = $('<button>', {'text': 'copy'})


$("#input_todo").keypress(function (key) {
    if (key.which == 13) {
        // let row = document.createElement("div")
        let row = $("<div>")
        //Set up left-side of list (entry)
        row.addClass("row row-entry")
        // let left_side = document.createElement("span")
        let left_side = $("<span>", { "text": $("#input_todo").val(), "css": { "color": $("#select_priority").val() } })
        // left_side.innerText = $("#input_todo").val()
        // left_side.style.color = $("#select_priority").val()
        left_side.hover(function () {
            $(this).css("cursor", "pointer")
        })
        row.append(left_side)
        //Set up right-side of list (date)
        let date = new Date()
        let year = date.getFullYear()
        let month = date.getMonth()
        let day = date.getDay()
        // let right_side = document.createElement("span")
        // right_side.innerText = month + "/" + day + "/" + year
        let right_side = $("<span>", { "text": month + "/" + day + "/" + year })
        row.append(right_side)
        $("#todolist").append(row)
        left_side.mousedown(function (event) {
            console.log("left_side.css('text-decoration')= " + left_side.css("text-decoration"))
            if (left_side.css("text-decoration").includes("line-through")) {
                console.log("trigger remove")
                row.remove()
            } else {
                left_side.css({ "text-decoration": "line-through", "color": "rgb(50, 50, 50)" })
                $("#todolist").append(row)
            }
        })
    }
})
$("#scribe").click(function () {
    // let row = document.createElement("div")
    let row = $("<div>")
    //Set up left-side of list (entry)
    row.addClass("row row-entry")
    // let left_side = document.createElement("span")
    let left_side = $("<span>", { "text": $("#input_todo").val(), "css": { "color": $("#select_priority").val() } })
    // left_side.innerText = $("#input_todo").val()
    // left_side.style.color = $("#select_priority").val()
    left_side.hover(function () {
        $(this).css("cursor", "pointer")
    })
    row.append(left_side)
    //Set up right-side of list (date)
    let date = new Date()
    let year = date.getFullYear()
    let month = date.getMonth()
    let day = date.getDay()
    // let right_side = document.createElement("span")
    // right_side.innerText = month + "/" + day + "/" + year
    let right_side = $("<span>", { "text": month + "/" + day + "/" + year })
    row.append(right_side)
    $("#todolist").append(row)
    left_side.mousedown(function (event) {
        console.log(event.target)
        if (left_side.children.length == 0) {
            left_side.innerHTML = left_side.innerText.strike()
            left_side.style.color = "rgb(75, 75, 75)"
            row.remove()
            $("#todolist").append(row)
        } else {
            console.log("strike detected")
            row.remove()
        }
    })
})