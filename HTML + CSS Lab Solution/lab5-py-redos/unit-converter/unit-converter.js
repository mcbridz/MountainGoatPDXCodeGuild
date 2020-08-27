let run_func = document.querySelector("#calc_but")
let value = document.querySelector("#value")
let src_units = document.querySelector("#src_units")
let dest_units = document.querySelector("#dest_units")
let output_div = document.querySelector("#output_div")

let meters_to_X = { "ft": 3.28, "mi": 0.0000621, "in": 39.37, "yd": 1.09361, "km": 0.001 }
let feet_to_X = { "m": 0.3048, "km": 0.0003048, "in": 12, "yd": 0.333, "mi": 0.0001894 }
let miles_to_X = { "m": 1609.344, "km": 1.609344, "in": 63360, "yd": 1760, "ft": 5280 }
let kilom_to_X = { "m": 1000, "in": 39370, "ft": 3280.84, "yd": 1093.61, "mi": 0.6214 }
let inches_to_X = { "m": 0.0254, "km": 0.0000254, "ft": 0.0833, "yd": 0.0278, "mi": 0.0000158 }
let yards_to_X = { "m": 0.9144, "km": 0.0009144, "in": 36, "ft": 3, "mi": 0.00057 }

let possible_conversions = ["m", "mi", "km", "in", "yd", "ft"]

let conversion_table = { "m": meters_to_X, "ft": feet_to_X, "mi": miles_to_X, "km": kilom_to_X, "in": inches_to_X }

function convert(input_units, input_value, output_units) { // "m", "1", "km" => 1000
    let conversion_factor = conversion_table[input_units][output_units]
    return input_value * conversion_factor
}

run_func.onclick = function () { // "m", "1", "km" => 1000
    let input_value = value.value
    let src = src_units.value
    let dest = dest_units.value
    let output_value = convert(src, input_value, dest)
    output_div.innerText = `${input_value} ${src} = ${output_value} ${dest}`
}