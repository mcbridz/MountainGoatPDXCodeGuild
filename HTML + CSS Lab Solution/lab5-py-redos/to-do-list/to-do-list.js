$("#input_todo").keypress(function (key) {
    if (key.which == 13) {
        let row = document.createElement("div")
        //Set up left-side of list (entry)
        $(row).addClass("row row-entry")
        let left_side = document.createElement("span")
        left_side.innerText = $("#input_todo").val()
        left_side.style.color = $("#select_priority").val()
        $(left_side).mousedown(function () {
            left_side.innerHTML = left_side.innerText.strike()
            left_side.style.color = "rgb(75, 75, 75)"
        })
        $(left_side).hover(function () {
            $(this).css("cursor", "pointer")
        })
        $(row).append(left_side)
        //Set up right-side of list (date)
        let right_side = document.createElement("span")
        let date = new Date()
        let year = date.getFullYear()
        let month = date.getMonth()
        let day = date.getDay()
        right_side.innerText = month + "/" + day + "/" + year
        $(row).append(right_side)
        $("#todolist").append(row)
    }
})
$("#scribe").click(function () {
    let row = document.createElement("div")
    //Set up left-side of list (entry)
    $(row).addClass("row row-entry")
    let left_side = document.createElement("span")
    left_side.innerText = $("#input_todo").val()
    left_side.style.color = $("#select_priority").val()
    $(left_side).mousedown(function () {
        left_side.innerHTML = left_side.innerText.strike()
        left_side.style.color = "rgb(75, 75, 75)"
    })
    $(left_side).hover(function () {
        $(this).css("cursor", "pointer")
    })
    $(row).append(left_side)
    //Set up right-side of list (date)
    let right_side = document.createElement("span")
    let date = new Date()
    let year = date.getFullYear()
    let month = date.getMonth()
    let day = date.getDay()
    right_side.innerText = month + "/" + day + "/" + year
    $(row).append(right_side)
    $("#todolist").append(row)
})