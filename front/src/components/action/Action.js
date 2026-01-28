import Swal from 'sweetalert2';

export const handleDeleteRow = (id, deleteRow) => {
    Swal.fire({
        title: `Удалить id: ${id}?`,
        text: 'Вы не сможете отменить это действие!',
        icon: 'warning',
        showCancelButton: true,
        confirmButtonText: 'Да, удалить!',
        cancelButtonText: 'Отмена',
    }).then(result => {
        if (result.isConfirmed) {
            deleteRow(id);
        }
    });
};

export const handleDeleteLog = (msg, freeCanvas) => {
    Swal.fire({
        title: `Удалить лог?`,
        text: 'Вы не сможете отменить это действие!',
        icon: 'warning',
        showCancelButton: true,
        confirmButtonText: 'Да, удалить!',
        cancelButtonText: 'Отмена',
    }).then(async result => {
        if (result.isConfirmed) {
            await freeCanvas();
        }
    });
};
