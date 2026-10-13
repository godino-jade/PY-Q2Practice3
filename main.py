from pyscript import document

def checkNum(e):

    num_bers = ["8", "11", "12", "28", "31"]

    num1 = document.getElementById("num1").value
    name = "Renn Pogi"

    confirm_num = num1 in num_bers

    message = (f'Sorry{name}, your number is not found.' , f'Yey! {name}, your number is found.')

    document.getElementById("output1").innerHTML = message[confirm_num]