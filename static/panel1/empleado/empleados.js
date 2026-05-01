const API = 'http://localhost:8000/api';

async function cargarEmpleados() {
    try {
        const res = await fetch(`${API}/empleado/`);
        const empleados = await res.json();
        const grid = document.getElementById('empleados-grid');
        grid.innerHTML = '';
        empleados.forEach(emp => {
            if (emp.Nombre === 'admin') return;
            const card = document.createElement('div');
            card.className = 'empleado-card';
            card.onclick = () => verEmpleado(emp);
            card.innerHTML = `
                <img src="https://cdn-icons-png.flaticon.com/512/1077/1077114.png" alt="${emp.Nombre}" class="card-img">
                <div class="nombre-emp">${emp.Nombre} ${emp.Apellido}</div>
            `;
            grid.appendChild(card);
        });
    } catch (err) { console.error('Error:', err); }
}

function verEmpleado(emp) {
    document.getElementById('nombre-value').textContent = emp.Nombre;
    document.getElementById('apellidos-value').textContent = emp.Apellido;
    document.getElementById('telefono-value').textContent = emp.Telefono || '-';
    document.getElementById('salario-value').textContent = emp.Pago_mes ? `$${parseFloat(emp.Pago_mes).toLocaleString('es-MX', {minimumFractionDigits:2})}` : '-';
    document.getElementById('panel-info').style.display = 'block';
}

function cerrarInfo() { document.getElementById('panel-info').style.display = 'none'; }

async function agregarEmpleado() {
    const nombre = prompt('Nombre:'); if (!nombre) return;
    const apellido = prompt('Apellido:');
    const telefono = prompt('Telefono:');
    const direccion = prompt('Direccion:');
    const rfc = prompt('RFC:');
    const pago = prompt('Pago mensual:');
    const contrasena = prompt('Contrasena:');
    try {
        await fetch(`${API}/empleado/`, {
            method: 'POST', headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ Nombre: nombre, Apellido: apellido, Telefono: telefono,
                Direccion: direccion, RFC: rfc, Pago_mes: parseFloat(pago) || 0, contrasena })
        });
        cargarEmpleados();
    } catch (err) { alert('Error al agregar empleado'); }
}

document.addEventListener('DOMContentLoaded', () => {
    cargarEmpleados();
    document.getElementById('btn-agregar').onclick = agregarEmpleado;
});
