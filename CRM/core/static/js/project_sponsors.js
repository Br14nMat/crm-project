const sponsorName = document.getElementById("sponsor_name");
const sponsorCardsContainer = document.getElementById("sponsor-cards-container");

const listSponsors = async () => {
    try {
        const response = await fetch(window.location.href + "/sponsors/" + sponsorName.value);
        const data = await response.json();

        // Limpiar el contenedor antes de agregar nuevas tarjetas
        sponsorCardsContainer.innerHTML = '';

        data.sponsors.forEach((sponsor) => {
            const card = document.createElement("div");
            card.className = "col";
            card.innerHTML = `
                <div class="card">
                    <h5 class="card-header">${sponsor.nit}</h5>
                    <div class="card-body d-flex justify-content-between">
                        <div>
                            <h5 class="card-title">${sponsor.name}</h5>
                        </div>
                        <div class="text-right">
                            <button type="submit" class="btn btn-secondary" name="link_sponsor" value="${sponsor.nit}">Agregar</button>
                        </div>
                    </div>
                </div>
            `;
            sponsorCardsContainer.appendChild(card);
        });

        console.log(data);
    } catch (error) {
        console.log(error);
    }
};

sponsorName.addEventListener("keyup", listSponsors);
