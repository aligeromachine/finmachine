import Swal from 'sweetalert2';

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

export const handleRow = (msg, id, handle) => {
    Swal.fire({
        title: `${msg} id: ${id}?`,
        text: 'Вы не сможете отменить это действие!',
        icon: 'warning',
        showCancelButton: true,
        confirmButtonText: 'Да!',
        cancelButtonText: 'Отмена',
    }).then(result => {
        if (result.isConfirmed) {
            handle(id);
        }
    });
};

export const handleDeleteRow = (id, deleteRow) => {
    handleRow('Удалить', id, deleteRow);
};

export const errValidMessage = () => {
    Swal.fire({
        title: `Ошибка валидации!`,
        icon: 'warning',
        showCancelButton: false,
        confirmButtonText: 'OK',
    }).then(result => {});
};
