var inventory = document.getElementById('inventory');
// var woodStock = document.getElementById('woodStock');
var woodStock, material, price;

function Product(name, price, stock) {
    this.checked = false;
    this.name = name;
    this.stock = stock;
    this.price = price;
    this.adjustStock = function(num) {
        this.stock -= num;
    };
    this.inStock = function() {
        return this.stock > 0;
    };
}

// this works for code below
// var materials = [new Product('Wood', 15, 10)];

var materials = [];
populateInventoryDOM();
// populateInventory();

// Direct DOM manipulation >>> safer approach
function populateInventoryDOM() {

    for (var i=0; i<materials.length; i++) {
        var newProdRow = document.createElement('tr'); //makes a tr

        var checkboxCell = document.createElement('td');
        var checkbox = document.createElement('input');
        checkbox.type = "checkbox"; //sets the attribute
        checkbox.checked = materials[i].checked;
        checkboxCell.appendChild(checkbox);
        newProdRow.appendChild(checkboxCell);

        //name column
        var nameCol = document.createElement('td');
        var nameText = document.createTextNode(materials[i].name);
        nameCol.appendChild(nameText); //better practice to add text
        newProdRow.appendChild(nameCol);

        //price column
        var priceCol = document.createElement('td');
        var priceText = document.createTextNode('$' + materials[i].price);
        priceCol.appendChild(priceText);
        newProdRow.appendChild(priceCol);

        //stock column
        var stockCol = document.createElement('td');
        stockCol.className = materials[i].inStock();
        var stockText = document.createTextNode(materials[i].stock);
        stockCol.appendChild(stockText);
        newProdRow.appendChild(stockCol);

        inventory.appendChild(newProdRow);
    }
}

function populateInventory() {
    // loop through materials
    // Add a row for each item in materials
    // Make sure that stock class reflects inStock
    // Make sure that checkbox status reflects checked
    for (var i = 0; i < materials.length; i++) {
        var newRow = "<tr>";
        newRow += "<td><input type='checkbox' /></td>";
        newRow += "<td>" + materials[i].name + "</td>";
        newRow += "<td>$" + materials[i].price + "</td>";
        newRow += "<td class=' " + materials[i].inStock() + " '>" + materials[i].stock + "</td>";
        newRow += "</tr>";
        inventory.innerHTML += newRow;
    }
}

function checkAll(checkbox) {
    var inputs = inventory.getElementsByTagName('input');
    for (var i = 0; i < inputs.length; i++) {
        if (inputs[i].type == 'checkbox') {
            inputs[i].checked = checkbox.checked;
        }
    }
}

function removeStock() {
    // var woodStock = document.getElementById('woodStock');
    rows = inventory.getElementsByTagName('tr');

    for (var i = 0; i < rows.length; i++) {
        var inputs = rows[i].getElementsByTagName('input');
        if (inputs[0].type == 'checkbox') {
            if (inputs[0].checked) {
                //Flip the status of the stock column
                var materialText = rows[i].firstElementChild.nextSibling;
                materialText.className = 'falseText';
                var priceText = materialText.nextSibling;
                priceText.className = 'falseText';
                var stockText = rows[i].lastElementChild;
                stockText.className = 'false';
                // stock.textContent = 'No';
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
                var materialText = rows[i].firstElementChild.nextSibling;
                materialText.className = 'trueText';
                var priceText = materialText.nextSibling;
                priceText.className = 'trueText';
                var stockText = rows[i].lastElementChild;
                stockText.className = 'true';

                // stock.textContent = 10;
                // inputs[0].checked = false;
            }
        }
    }
}

// ! need to add to materials list
function addNewStock() {
    material = document.getElementById('material').value;
    price = document.getElementById('price').value;

    if (material === "" || price === "" || isNaN(price)) {
        alert("invalid input");
        return;
    }
    var newRow = "<tr>";
        newRow += "<td><input type='checkbox'></td>";
        newRow += "<td>" + material + "</td>";
        newRow += "<td>$" + price + "</td>";
        newRow += "<td class='true'>10</td>";
        newRow += "</tr>";

        inventory.innerHTML += newRow;

    // you have to grab it again because assigning it above only has a reference to the html object
    document.getElementById('material').value = '';
    document.getElementById('price').value = '';
    // materials.push(new Product(material, 10, price));
}

// function mock_addNewStock() {
//     material = document.getElementById('material').value;
//     price = document.getElementById('price').value;

//     if (material === "" || price === "" || isNaN(price)) {
//         alert("invalid input");
//         return;
//     }
//     for (var i = 0; i < 5; i++) {
//         var newRow = "<tr>";
//         newRow += "<td><input type='checkbox'></td>";
//         newRow += "<td>" + material + "</td>";
//         newRow += "<td>$" + price + "</td>";
//         newRow += "<td class='false'>No</td>";
//         newRow += "</tr>";
//         inventory.innerHTML += newRow;
//     }

//     // you have to grab it again because assigning it above only has a reference to the html object
//     document.getElementById('material').value = '';
//     document.getElementById('price').value = '';
// }


// Create XMLHttpRequest object
var newRequest = new XMLHttpRequest();
// console.log(newRequest);
newRequest.onload = function() {
    if (newRequest.status === 200) {
        var response = JSON.parse(newRequest.responseText);
        // console.log(response);
        // console.log(response.items);
        var items = response.inventory.item

        for (var i = 0; i < items.length; i++) {
            var product = new Product (
                items[i].name,
                items[i].price,
                items[i].numInStock
            )
            materials.push(product);
        }
        populateInventoryDOM();
    }
};

newRequest.open('Get', 'data/stock.json', true); // prepare the request
newRequest.send(null); // send the request




