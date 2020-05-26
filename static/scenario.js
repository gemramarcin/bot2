


var container = document.querySelector(".container");
var e = document.getElementById("scenario-select");
console.log(e)

function createSingleInput(name) {
    var input = document.createElement("input");
    input.id = name;
    input.type = "text";
    input.name = name;
    var label = document.createElement("label");
    label.innerHTML = name + ": ";
    label.setAttribute("for", "name");

    var div = document.createElement("div");
    div.classList.add("container__item");
    div.appendChild(label);
    div.appendChild(input);

    container.appendChild(div);
}



function changeInput() {

    while (container.hasChildNodes()) {
        container.removeChild(container.lastChild);
    }




    var value = e.options[e.selectedIndex].value
    console.log(value)

    if (value == "1") {

        createSingleInput("targetIp");
        createSingleInput("minPortRange");
        createSingleInput("maxPortRange");
    }
    else if (value == "2"){
        createSingleInput("targetIp");
        createSingleInput("port")
    }
    else if (value == "3"){
        createSingleInput("targetIp");
        createSingleInput("gatewayIp");
    }

    else if (value == "4"){
        createSingleInput("targetIp");
        createSingleInput("number Of Packets");
    }

    let data = document.querySelector(".data");
    data.innerHTML = "result: "




}

e.addEventListener("change", changeInput);

