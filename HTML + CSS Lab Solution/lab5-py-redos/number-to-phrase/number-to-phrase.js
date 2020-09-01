let num_raw = document.querySelector("#num-input")
let phrase_but = document.querySelector("#gen_but")
let output_div = document.querySelector("#output_div")

//checking for code run
console.log(phrase_but)

let ones_not_teens = {
    0: "",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten"
}

let tweens = {
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen"
}

let tens_not_tweens = {
    2: "twenty",
    3: "thirty",
    4: "fourty",
    5: "fifty",
    6: "sixty",
    7: "seventy",
    8: "eighty",
    9: "ninety"
}

let distal_digits = {
    1: "",
    2: " thousand",
    3: " million",
    4: " billion",
    5: " trillion",
    6: " quadrillion"
}

function number_of_digits(input_num) {
    tmp_str = input_num.toString()
    return tmp_string.length
}

function hundreds_translate(input_num, triplets) {
    if (input_num == 0) { return "" }

    let arr_num = input_num.toString().split("")
    let int_num = parseInt(input_num)
    let return_string = ""
    if (int_num < 10) {
        if (triplets <= 1) {
            return_string += " and "
        }
        return_string += ones_not_teens[int_num]
        if (triplets > 1) {
            return_string += `${distal_digits[triplets]} `
        }
        return return_string
    }
    else if (int_num < 20) {
        return_string += tweens[int_num]
        return_string += `${distal_digits[triplets]} `
        return return_string
    }
    else if (int_num < 100) {
        return_string += tens_not_tweens[parseInt(arr_num[0])]
        if (arr_num[1] != 0) {
            return_string += '-'
            return_string += ones_not_teens[parseInt(arr_num[1])]
        }
        return_string += `${distal_digits[triplets]} `
        return return_string
    }
    else {
        return_string += ones_not_teens[parseInt(arr_num[0])]
        return_string += " hundred"
        if (arr_num[1] == '0' && arr_num[2] == '0') {
            return_string += distal_digits[triplets]
            return_string += " "
            return return_string
        }
        if (arr_num[1] == '0') {
            return_string += " and "
            return_string += ones_not_teens[parseInt(arr_num[2])]
            return_string += `${distal_digits[triplets]} `
            return return_string
        }
        else if (arr_num[1] == '1') {
            return_string += ` ${tweens[10 + parseInt(arr_num[2])]}`
            return_string += `${distal_digits[triplets]} `
            return return_string
        }
        else {
            return_string += ` ${tens_not_tweens[parseInt(arr_num[1])]}`
            if (parseInt(arr_num[2]) != 0) {
                return_string += `-${ones_not_teens[parseInt(arr_num[2])]}`
            }
            return_string += `${distal_digits[triplets]} `
            return return_string
        }
        // return return_string
    }

}

function break_and_translate(input_num) {
    console.log(input_num)
    if (input_num == 0) {
        return ""
    }
    let arr_num = input_num.toString().split("")
    let int_num = parseInt(input_num)
    while (arr_num.length % 3 != 0) {
        arr_num.reverse()
        arr_num.push('0')
        arr_num.reverse()
    }
    let return_string = ""
    let i = 0
    let triplets = parseInt(arr_num.length / 3)
    while (i < arr_num.length - 1) {
        let broken_off_hundreds = parseInt(arr_num.slice(i, i + 3).join(""))
        return_string += hundreds_translate(broken_off_hundreds, triplets)
        triplets -= 1
        i += 3
    }
    return return_string
}

phrase_but.onclick = function () {
    let input_num = num_raw.value
    console.log(input_num)
    let output_str = break_and_translate(input_num)
    console.log(output_str)
    output_div.innerText = output_str
}