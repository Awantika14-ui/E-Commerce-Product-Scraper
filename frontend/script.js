async function search() {
    const query = document.getElementById("search").value;

    const res = await fetch(`http://127.0.0.1:5000/api/search?q=${query}`);
    const data = await res.json();

    const resultsDiv = document.getElementById("results");
    resultsDiv.innerHTML = "";

    if (data.length === 0) {
        resultsDiv.innerHTML = "<p>No products found</p>";
        return;
    }

    data.forEach(p => {
        const card = document.createElement("div");
        card.className = "card";

        card.innerHTML = `
            <img src="${p.image}" />
            <h3>${p.name}</h3>
            <p>${p.price}</p>
            <p>⭐ ${p.rating}</p>
            <a href="${p.link}" target="_blank">View Details</a>
        `;

        resultsDiv.appendChild(card);
    });
}
