


var container = document.querySelector(".container");
var e = document.getElementById("scenario-select");
console.log(e)

function createInputIP() {
    var input = document.createElement("input");
    input.id = "targetIp"
    input.type = "text";
    input.name = "targetIp";
    var label = document.createElement("label");
    label.innerHTML = "Target IP: "
    label.setAttribute("for", "tagetIp");

    var div = document.createElement("div");
    div.classList.add("container__item");
    div.appendChild(label);
    div.appendChild(input);

    container.appendChild(div);
}

function createPort(){
    var input = document.createElement("input");
    input.id = "port"
    input.type = "text";
    input.name = "port";
    var label = document.createElement("label");
    label.innerHTML = "port: "
    label.setAttribute("for", "port");
    // container.appendChild(label);
    // container.appendChild(input);

    var div = document.createElement("div");
    div.classList.add("container__item");
    div.appendChild(label);
    div.appendChild(input);

    container.appendChild(div);
    
}

function createGatewayIp(){
    var input = document.createElement("input");
    input.id = "gatewayIp"
    input.type = "text";
    input.name = "gatewayIp";
    var label = document.createElement("label");
    label.innerHTML = "Gateway IP: "
    label.setAttribute("for", "gatewayIp");
    // container.appendChild(label);
    // container.appendChild(input);

    var div = document.createElement("div");
    div.classList.add("container__item");
    div.appendChild(label);
    div.appendChild(input);

    container.appendChild(div);
}


function createMaxPortRange(){

    var div = document.createElement("div");
    div.classList.add("container__item");


    var input = document.createElement("input");
    input.id = "maxPortRange"
    input.type = "text";
    input.name = "maxPortRange";
    var label = document.createElement("label");
    label.innerHTML = "maxPortRange: "
    label.setAttribute("for", "maxPortRange");

    div.appendChild(label);
    div.appendChild(input);

    container.appendChild(div);
}

function createMinPortRange(){

    var div = document.createElement("div");
    div.classList.add("container__item");


    var input = document.createElement("input");
    input.id = "minPortRange"
    input.type = "text";
    input.name = "minPortRange";
    var label = document.createElement("label");
    label.innerHTML = "minPortRange: "
    label.setAttribute("for", "minPortRange");

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
        createInputIP();
        createMinPortRange();
        createMaxPortRange();
    }
    else if (value == "2"){
        createInputIP();
        createPort();
    }
    else if (value == "3"){
        createInputIP();
        createGatewayIp();
    }


}

e.addEventListener("change", changeInput);

