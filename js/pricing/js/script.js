var inventory = document.getElementById('inventory');
// var woodStock = document.getElementById('woodStock');
var woodStock, material, price;

function checkAll(checkbox) {
    var inputs = inventory.getElementsByTagName('input');
    for (var i = 0; i < inputs.length; i++) {
        if (inputs[i].type == 'checkbox') {
            inputs[i].checked = checkbox.checked
        }
    }
}

function Product(name, stock, price) {
    this.checked = false;
    this.name = name;
    this.stock = stock;
    this.price = price;

    this.adjustStock = function(num) {
        this.stock -= num;
    }
    this.inStock = function() {
        return this.stock > 0;
    }
}
var materials = [new Product('wood', 10, 15)];

function removeStock() {
    // var woodStock = document.getElementById('woodStock');
    rows = inventory.getElementsByTagName('tr');

    for (var i = 0; i < rows.length; i++) {
        var inputs = rows[i].getElementsByTagName('input'); //this will get a list and we know this by the plural Elements
        // console.log(inputs[0]);
        if (inputs[0].type == 'checkbox') {
            if (inputs[0].checked) {
                //Flip the status of the stock column
                var stock = rows[i].lastElementChild;
                stock.className = 'false';
                stock.textContent = 'No';
                // inputs[0].checked = false;
            }
        }
    }
}

function addStock() {
    // var woodStock = document.getElementById('woodStock');
    rows = inventory.getElementsByTagName('tr');

    for (var i = 0; i < rows.length; i++) {
        var inputs = rows[i].getElementsByTagName('input'); //this will get a list and we know this by the plural Elements
        // console.log(inputs[0]);
        if (inputs[0].type == 'checkbox') {
            if (inputs[0].checked) {
                //Flip the status of the stock column
                var stock = rows[i].lastElementChild;
                stock.className = 'true';
                stock.textContent = 'Yes';
                // inputs[0].checked = false;
            }
        }
    }
}

function addNewStock() {
    material = document.getElementById('material').value;
    price = document.getElementById('price').value;

    if (material === "" || price === "" || isNaN(price)) {
        alert("invalid input")
        return
    }
    var newRow = "<tr>";
        newRow += "<td><input type='checkbox'></td>";
        newRow += "<td>" + material + "</td>";
        newRow += "<td>$" + price + "</td>";
        newRow += "<td class='false'>No</td>";
        newRow += "</tr>";

        inventory.innerHTML += newRow;

    // you have to grab it again because assigning it above only has a reference to the html object
    document.getElementById('material').value = '';
    document.getElementById('price').value = '';
}
