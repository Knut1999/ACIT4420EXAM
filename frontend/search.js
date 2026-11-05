async function search() {
    const urlPost = "http://localhost:8000/items/";
    const responsePost = await fetch(urlPost, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            destination: document.getElementById("destinations").value,
            budgetType: document.getElementById("budgetType").value,
            budgetSum: document.getElementById("budgetSum").value,
            preferredDepartureTime: document.getElementById("preferredDepartureTime").value
        }),
    });
    const offers = await responsePost.json();

    const table = document.getElementById("offersTable");
    table.innerHTML = "";

    offers.forEach((offer, index) => {
        const row = table.insertRow();

    row.innerHTML = `
        <td>${index + 1}</td>
        <td>${offer.companyName}</td>
        <td>${offer.destination}</td>
        <td>${offer.travelDate}</td>
        <td>${offer.departureTime}</td>
        <td>${offer.duration}</td>
        <td>${offer.arrivalTime}</td>
        <td>${offer.price}</td>
        <td>${offer.transfers}</td>
        <td>${offer.luggageAllowance}</td>
        <td>${offer.changeability}</td>
        <td>${offer.refundability}</td>
        <td>${offer.availableSeats}</td>
        <td>${offer.customerRating}</td>
        <td>${offer.environmentalMeasure}</td>
        <td>${offer.score.toFixed(3)}</td>
        `;
    });
}
