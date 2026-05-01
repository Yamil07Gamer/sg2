const API = 'http://localhost:8000/api';

async function cargarPlatillos() {
    try {
        const res = await fetch(`${API}/platillo/`);
        const platillos = await res.json();
        const grid = document.getElementById('platillos-grid');
        grid.innerHTML = '';
        platillos.forEach(p => {
            const card = document.createElement('div');
            card.className = 'platillo-card';
            card.onclick = () => verPlatillo(p);
            card.innerHTML = `
                <img src="https://cdn-icons-png.flaticon.com/512/857/857681.png" alt="${p.Nombre}" class="card-img">
                <div class="nombre-pla">${p.Nombre}</div>
            `;
            grid.appendChild(card);
        });
    } catch (err) { console.error('Error:', err); }
}

function verPlatillo(p) {
    document.getElementById('codigo-value').textContent = p.ID_platillo;
    document.getElementById('nombre-value').textContent = p.Nombre;
    document.getElementById('descripcion-value').textContent = p.Descripcion || '-';
    document.getElementById('precio-value').textContent = `$${parseFloat(p.Precio).toFixed(2)}`;
    document.getElementById('panel-info').style.display = 'block';
}

function cerrarInfo() { document.getElementById('panel-info').style.display = 'none'; }

async function agregarPlatillo() {
    const nombre = prompt('Nombre del platillo:'); if (!nombre) return;
    const descripcion = prompt('Descripcion:');
    const precio = prompt('Precio:');
    try {
        await fetch(`${API}/platillo/`, {
            method: 'POST', headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ Nombre: nombre, Descripcion: descripcion, Precio: parseFloat(precio) || 0 })
        });
        cargarPlatillos();
        cerrarInfo();
    } catch (err) { alert('Error al agregar'); }
}

document.addEventListener('DOMContentLoaded', () => {
    cargarPlatillos();
    document.getElementById('btn-agregar').onclick = agregarPlatillo;
});
