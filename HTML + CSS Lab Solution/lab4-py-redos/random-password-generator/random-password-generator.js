let num_input = document.querySelector("#num_chars")
let generate_but = document.querySelector("#gen_but")
let output_fld = document.querySelector("#pwd-text")

function randint(a, b) {
    let delta = b - a
    let randomizer = parseInt(Math.random() * delta) + a
    return randomizer
}

function generateUpper() {
    return String.fromCharCode(randint(65, 91))
}

function generateLower() {
    return String.fromCharCode(randint(97, 123))
}

function generateSpChr() {
    return String.fromCharCode(randint(33, 48))
}

function generateNum() {
    return parseInt(randint(0, 10))
}


generate_but.onclick = function () {
    let num_chars = num_input.value
    let i = 0
    output_txt = ""
    while (i < num_chars) {
        let roullete = [generateUpper(), generateLower(), generateSpChr(), generateNum()]
        output_txt += roullete[randint(0, 4)]
        i++
    }
    output_fld.value = output_txt
}