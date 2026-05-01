const API = 'http://localhost:8000/api';
let orden = [];
const idEmpleadoSesion = parseInt(sessionStorage.getItem('id_empleado'));

async function cargarPlatillos() {
    try {
        const res = await fetch(`${API}/platillo/`);
        const platillos = await res.json();
        const grid = document.getElementById('platillos-grid');
        grid.innerHTML = '';
        platillos.forEach(p => {
            const card = document.createElement('div');
            card.className = 'platillo-card';
            card.onclick = () => agregarPlatillo(p);
            card.innerHTML = `
                <img src="https://cdn-icons-png.flaticon.com/512/857/857681.png" alt="${p.Nombre}" class="card-img">
                <div class="nombre-pla">${p.Nombre}<br><small>$${parseFloat(p.Precio).toFixed(2)}</small></div>
            `;
            grid.appendChild(card);
        });
    } catch (err) { console.error('Error:', err); }
}

function agregarPlatillo(p) {
    const existing = orden.find(i => i.id === p.ID_platillo);
    if (existing) { existing.cantidad++; existing.total = existing.cantidad * existing.precio; }
    else { orden.push({ id: p.ID_platillo, nombre: p.Nombre, precio: parseFloat(p.Precio), cantidad: 1, total: parseFloat(p.Precio) }); }
    actualizarOrden();
}

function aumentarCantidad(id) {
    const item = orden.find(i => i.id === id);
    if (item) { item.cantidad++; item.total = item.cantidad * item.precio; actualizarOrden(); }
}

function disminuirCantidad(id) {
    const item = orden.find(i => i.id === id);
    if (item && item.cantidad > 1) { item.cantidad--; item.total = item.cantidad * item.precio; actualizarOrden(); }
}

function eliminarItem(id) { orden = orden.filter(i => i.id !== id); actualizarOrden(); }

function actualizarOrden() {
    const lista = document.getElementById('orden-lista');
    lista.innerHTML = '';
    const totalGeneral = orden.reduce((s, i) => s + i.total, 0);
    orden.forEach(item => {
        const div = document.createElement('div');
        div.className = 'orden-item';
        div.innerHTML = `
            <div class="item-nombre">${item.nombre}</div>
            <div class="item-total">$${item.total.toFixed(2)}</div>
            <button class="item-btn item-btn-mas" onclick="aumentarCantidad(${item.id})">+</button>
            <div class="item-cantidad">${item.cantidad}</div>
            <button class="item-btn item-btn-menos" onclick="disminuirCantidad(${item.id})">-</button>
            <button class="item-btn item-btn-eliminar" onclick="eliminarItem(${item.id})">&times;</button>
        `;
        lista.appendChild(div);
    });
    document.getElementById('total-display').textContent = `TOTAL: $${totalGeneral.toFixed(2)}`;
}

function cancelarOrden() { if (confirm('Cancelar la orden?')) { orden = []; actualizarOrden(); } }

function pagarOrden() {
    if (orden.length === 0) { alert('La orden esta vacia'); return; }
    const total = orden.reduce((s, i) => s + i.total, 0);
    document.getElementById('modal-total').value = total.toFixed(2);
    document.getElementById('input-cambio').value = '0.00';
    document.getElementById('modal-overlay').style.display = 'flex';
}

function cerrarModal() { document.getElementById('modal-overlay').style.display = 'none'; }

async function confirmarPago() {
    const nombreCliente = document.getElementById('input-cliente').value.trim();
    const tipoPago = document.getElementById('input-tipopago').value;
    const totalOrden = orden.reduce((s, i) => s + i.total, 0);
    const totalRecibido = parseFloat(document.getElementById('modal-total').value) || 0;
    const cambio = document.getElementById('input-cambio').value;
    const tipoOrden = document.getElementById('input-tipoorden').value;

    if (!nombreCliente || !tipoPago) { alert('Completa todos los campos'); return; }

    try {
        const resCliente = await fetch(`${API}/cliente/`, {
            method: 'POST', headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ Nombre: nombreCliente, Correo: '', Telefono: '', ID_mesa: null })
        });
        const dataCliente = await resCliente.json();

        const resOrden = await fetch(`${API}/orden/`, {
            method: 'POST', headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ Tipo_orden: tipoOrden, Total: totalOrden,
                Metodo_de_pago: tipoPago, Cambio: cambio, ID_cliente: dataCliente.id })
        });
        const dataOrden = await resOrden.json();

        for (const item of orden) {
            for (let i = 0; i < item.cantidad; i++) {
                await fetch(`${API}/compra/`, {
                    method: 'POST', headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ Id_empleado: idEmpleadoSesion, Id_orden: dataOrden.id, Id_platillo: item.id, cantidad: 1 })
                });
            }
        }

        // Registrar en En_sal como entrada
        await fetch(`${API}/ensal/`, {
            method: 'POST', headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ dinero: totalOrden, tipo: 'entrada', ID_orden: dataOrden.id })
        });

        alert('Orden registrada correctamente!');
        orden = []; actualizarOrden(); cerrarModal();
        document.getElementById('input-cliente').value = '';
    } catch (err) { alert('Error: ' + err.message); }
}

document.addEventListener('DOMContentLoaded', () => {
    cargarPlatillos();
    document.getElementById('btn-cancelar').onclick = cancelarOrden;
    document.getElementById('btn-pagar').onclick = pagarOrden;
    document.getElementById('btn-confirmar-pago').onclick = confirmarPago;
    document.getElementById('btn-cerrar-modal').onclick = cerrarModal;

    document.getElementById('modal-total').addEventListener('input', function() {
        const totalOrden = orden.reduce((s, i) => s + i.total, 0);
        const recibido = parseFloat(this.value) || 0;
        const cambio = recibido - totalOrden;
        document.getElementById('input-cambio').value = cambio >= 0 ? cambio.toFixed(2) : '0.00';
    });
});
