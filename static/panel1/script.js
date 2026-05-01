// Esperar a que el DOM esté completamente cargado
document.addEventListener('DOMContentLoaded', function() {
    
    // Verificar si el usuario está autenticado
    const isLoggedIn = sessionStorage.getItem('isLoggedIn');
    if (!isLoggedIn) {
        window.location.href = '../index.html';
        return;
    }

    // Obtener todos los botones
    const btnFinanzas = document.getElementById('btnFinanzas');
    const btnPedirOrden = document.getElementById('btnPedirOrden');
    const btnEmpleados = document.getElementById('btnEmpleados');
    const btnPlatillos = document.getElementById('btnPlatillos');
    const btnInventario = document.getElementById('btnInventario');
    const btnLogout = document.getElementById('btnLogout');

    // Event listeners para cada botón
    btnFinanzas.addEventListener('click', function() {
        window.location.href = 'finanzas/index.html';
    });

    btnPedirOrden.addEventListener('click', function() {
        window.location.href = 'pedirorden/index.html';
    });

    btnEmpleados.addEventListener('click', function() {
        window.location.href = 'empleado/index.html';
    });

    btnPlatillos.addEventListener('click', function() {
        window.location.href = 'platillo/index.html';
    });

    btnInventario.addEventListener('click', function() {
        window.location.href = 'inventario/index.html';
    });

    // Logout
    btnLogout.addEventListener('click', function() {
        const confirmar = confirm('¿Estás seguro que deseas cerrar sesión?');
        if (confirmar) {
            sessionStorage.removeItem('isLoggedIn');
            sessionStorage.removeItem('usuario');
            window.location.href = '../index.html';
        }
    });

    // Mostrar usuario conectado en consola
    const usuario = sessionStorage.getItem('usuario');
    if (usuario) {
        console.log('Usuario conectado:', usuario);
    }
});
