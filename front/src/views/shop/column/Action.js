import { deleteShopRow } from "../../../services/stateShop";
import Swal from "sweetalert2";

export const handleDelete = (id) => {
  Swal.fire({
    title: `Удалить id: ${id}?`,
    text: "Вы не сможете отменить это действие!",
    icon: "warning",
    showCancelButton: true,
    confirmButtonText: "Да, удалить!",
    cancelButtonText: "Отмена",
  }).then((result) => {
    if (result.isConfirmed) {
      deleteShopRow(id);
    }
  });
};

export const handleEdit = (id) => {
  console.log(id);
};
