const API = 'http://localhost:8000/api';

document.addEventListener('DOMContentLoaded', function () {
    const loginForm = document.getElementById('loginForm');

    loginForm.addEventListener('submit', async function (e) {
        e.preventDefault();
        const nombre = document.getElementById('usuario').value.trim();
        const contrasena = document.getElementById('password').value.trim();

        if (!nombre || !contrasena) {
            alert('Por favor, completa todos los campos');
            return;
        }

        try {
            const res = await fetch(`${API}/login`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ nombre, contrasena })
            });
            const data = await res.json();
            if (res.ok && data.ok) {
                sessionStorage.setItem('isLoggedIn', 'true');
                sessionStorage.setItem('usuario', nombre);
                sessionStorage.setItem('id_empleado', data.id_empleado);
                window.location.href = 'panel1/index.html';
            } else {
                alert('Usuario o contrasena incorrectos');
            }
        } catch (err) {
            alert('Error conectando con el servidor');
        }
    });

    const inputs = document.querySelectorAll('.form-input');
    inputs.forEach(input => {
        input.addEventListener('focus', function () { this.style.borderColor = '#00FFFF'; });
        input.addEventListener('blur', function () { this.style.borderColor = '#9CA3AF'; });
    });
});
