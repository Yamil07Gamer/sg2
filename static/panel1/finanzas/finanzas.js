const API = 'http://localhost:8000/api';

function fmt(n) {
    return parseFloat(n).toLocaleString('es-MX', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
}

async function cargarRegistros() {
    try {
        const res = await fetch(`${API}/ensal/`);
        const registros = await res.json();
        const lista = document.getElementById('registros-lista');
        lista.innerHTML = '';
        let acumulado = 0;
        registros.forEach(r => {
            acumulado += parseFloat(r.dinero);
            const div = document.createElement('div');
            div.className = `registro-row ${r.tipo === 'entrada' ? 'entrada' : 'salida'}`;
            const montoDisplay = Math.abs(parseFloat(r.dinero));
            div.innerHTML = `
                <span class="reg-tipo">${r.tipo.toUpperCase()}</span>
                <span class="reg-monto">$${fmt(montoDisplay)}</span>
                <span class="reg-acum">$${fmt(acumulado)}</span>
            `;
            lista.appendChild(div);
        });
        document.getElementById('total-value').textContent = `$${fmt(acumulado)}`;
    } catch (err) { console.error('Error:', err); }
}

async function agregarEntrada() {
    const monto = prompt('Ingrese el monto de entrada:');
    if (!monto || isNaN(monto) || parseFloat(monto) <= 0) { alert('Monto invalido'); return; }
    await fetch(`${API}/ensal/`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ dinero: parseFloat(monto), tipo: 'entrada' })
    });
    cargarRegistros();
}

async function agregarSalida() {
    const monto = prompt('Ingrese el monto de salida (positivo):');
    if (!monto || isNaN(monto) || parseFloat(monto) <= 0) { alert('Monto invalido'); return; }
    await fetch(`${API}/ensal/`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ dinero: -parseFloat(monto), tipo: 'salida' })
    });
    cargarRegistros();
}

document.addEventListener('DOMContentLoaded', () => {
    cargarRegistros();
    document.getElementById('btn-entrada').onclick = agregarEntrada;
    document.getElementById('btn-salida').onclick = agregarSalida;
});
