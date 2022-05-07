const btnDlete = document.querySelectorAll('.btn-delete');
const btnEdit = document.querySelectorAll('.btn-edit');

if(btnDlete) {
    const btnDeleteArray = Array.from(btnDlete);
    btnDeleteArray.forEach((btn) => {
    btn.addEventListener('click', (e) => {
        if(!confirm('Está seguro de Eliminar este item ?')) {
            e.preventDefault();
        }
    });
});
}