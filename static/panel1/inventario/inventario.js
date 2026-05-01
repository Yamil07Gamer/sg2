const API = 'http://localhost:8000/api';

async function cargarInventario() {
    try {
        const res = await fetch(`${API}/ingrediente/`);
        const items = await res.json();
        const grid = document.getElementById('inventario-grid');
        grid.innerHTML = '';
        items.forEach(item => {
            const card = document.createElement('div');
            card.className = 'inventario-card';
            card.onclick = () => verItem(item);
            card.innerHTML = `
                <img src="https://cdn-icons-png.flaticon.com/512/135/135620.png" alt="${item.Nombre}" class="card-img">
                <div class="nombre-item">${item.Nombre}</div>
            `;
            grid.appendChild(card);
        });
    } catch (err) { console.error('Error:', err); }
}

function verItem(item) {
    document.getElementById('codigo-value').textContent = item.ID_ingrediente;
    document.getElementById('nombre-value').textContent = item.Nombre;
    document.getElementById('descripcion-value').textContent = item.Descripcion || '-';
    document.getElementById('cantidad-value').textContent = item.Cantidad;
    document.getElementById('panel-info').style.display = 'block';
}

function cerrarInfo() { document.getElementById('panel-info').style.display = 'none'; }

async function agregarIngrediente() {
    const nombre = prompt('Nombre:'); if (!nombre) return;
    const descripcion = prompt('Descripcion:');
    const cantidad = prompt('Cantidad:');
    try {
        await fetch(`${API}/ingrediente/`, {
            method: 'POST', headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ Nombre: nombre, Descripcion: descripcion, Cantidad: parseInt(cantidad) || 0 })
        });
        cargarInventario();
        cerrarInfo();
    } catch (err) { alert('Error al agregar'); }
}

document.addEventListener('DOMContentLoaded', () => {
    cargarInventario();
    document.getElementById('btn-agregar').onclick = agregarIngrediente;
});
