(function () {
    const btnEliminar=document.querySelectorAll(".btnEliminar")

    btnEliminar.forEach(btn => {
        btn.addEventListener('click', (e)=>{
            const confirmacion = confirm('¿ Esta seguro que quiere eliminar esta solicitud ?');
            if(!confirmacion){
                e.preventDefault();
            }

        });
    });
})();
