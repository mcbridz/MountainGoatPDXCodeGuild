let num_scores = document.querySelector("#num_scores")
let btn_scores = document.querySelector("#btn_scores")
let score_flds = document.querySelector("#score_flds")
let info_flds = document.querySelector("#cont_scores")
let rand_btn = document.querySelector("#scores_rnd")
let grade = document.querySelector("#grade")
let clear_btn = document.querySelector("#clear")
let num_flds = 0

btn_scores.onclick = function () {
    num_flds = num_scores.value
    let prefix = '<div class="row" id="row'
    let midfix = '"><div class=col-2><input type="text" placeholder="score" class="container" id="grade'
    let postfix = '" \></div></div>'
    let arr_fld_html = []
    for (let i = 0; i < num_flds; i++) {
        let tmp_string = `${prefix}${i}${midfix}${i}${postfix}`
        arr_fld_html.push(tmp_string)
    }
    arr_fld_html.reverse()
    while (arr_fld_html.length != 0) {
        score_flds.innerHTML += arr_fld_html.pop()
    }
    rand_btn.hidden = false
    grade.hidden = false
    clear_btn.hidden = false
}

function randomGrade() {
    return parseInt(Math.random() * 51) + 50
}

rand_btn.onclick = function () {
    for (let i = 0; i < num_flds; i++) {
        let fld = document.querySelector(`#grade${i}`)
        grade = randomGrade()
        fld.value = `${grade}`
    }
}

grade.onclick = function () {
    let grades = { 5: 'F', 6: 'D', 7: 'C', 8: 'B', 9: 'A', 10: 'A' }
    let modifier = ""
    for (let i = 0; i < num_flds; i++) {
        let fld = document.querySelector(`#row${i}`)
        let grd = document.querySelector(`#grade${i}`)
        let tmp_grade = parseInt(grd.value)
        if (tmp_grade % 10 < 5) {
            modifier = "-"
        }
        else if (tmp_grade % 10 > 5) {
            modifier = "+"
        }
        if (grade != 100) {
            fld.innerHTML += `<div class= "col-1">${grades[parseInt(tmp_grade / 10)].toString()}${modifier}</div>`
            console.log(fld.innerHTML)
            grd = document.querySelector(`#grade${i}`)
            grd.value = `${tmp_grade}`
        }
        else {
            fld.innerHTML += `<div class= "col-1">A+</div>`
            grd = document.querySelector(`#grade${i}`)
            grd.value = `${tmp_grade}`
        }
    }
}

clear_btn.onclick = function () {
    grade = document.querySelector("#grade")
    score_flds = document.querySelector("#score_flds")
    score_flds.innerHTML = ""
    rand_btn.hidden = true
    grade.hidden = true
    clear_btn.hidden = true
}