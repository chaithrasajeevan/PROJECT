let outfits = JSON.parse(localStorage.getItem("outfits")) || [];

function saveOutfits() {
    localStorage.setItem("outfits", JSON.stringify(outfits));
}

// Add Outfit
function addOutfit() {
    let name = document.getElementById("outfitName").value;
    let img = document.getElementById("outfitImage").value;

    outfits.push({ name: name, image: img });
    saveOutfits();
    displayOutfits();

    alert("Outfit Added Successfully!");
}

// Display outfits
function displayOutfits() {
    let list = document.getElementById("outfitList");
    list.innerHTML = "";

    outfits.forEach((item, index) => {
        list.innerHTML += `
            <div class="outfit-card">
                <img src="${item.image}" width="100">
                <p>${item.name}</p>
                <button onclick="deleteOutfit(${index})">Delete</button>
            </div>
            <hr>
        `;
    });
}

displayOutfits();

// Delete
function deleteOutfit(index) {
    outfits.splice(index, 1);
    saveOutfits();
    displayOutfits();
}