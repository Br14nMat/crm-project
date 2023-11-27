const sponsorName = document.getElementById("sponsor_name");
const sponsorTable = document.getElementById("sponsor-table-body");

const listSponsors = async () => {
    try {
        const response = await fetch(window.location.href + "/sponsors/" + sponsorName.value);
        const data = await response.json();

        // Limpiar la tabla antes de agregar nuevos datos
        sponsorTable.innerHTML = '';

        data.sponsors.forEach((sponsor) => {
            const row = document.createElement("tr");
            row.innerHTML = `
                <td>${sponsor.nit}</td>
                <td>${sponsor.name}</td>
                <td>
                    <button type="submit" class="btn btn-secondary" name="link_sponsor" value="${sponsor.nit}">Agregar</button>
                </td>
            `;
            sponsorTable.appendChild(row);
        });

        console.log(data);
    } catch (error) {
        console.log(error);
    }
};

sponsorName.addEventListener("keyup", listSponsors);
