import React from "react";
import { handleDelete, handleEdit } from "./Action";
import st from "./row.module.css";

export const columnsShop = (openModal) => {
  const openWithEdit = async (id) => {
    await handleEdit(id);
    openModal();
  };

  return [
    {
      accessorKey: "id",
      header: "Id",
      size: 100,
    },
    {
      accessorKey: "created",
      header: "Created",
    },
    {
      accessorKey: "title",
      header: "Title",
    },
    {
      accessorKey: "address",
      header: "Address",
    },
    {
      accessorKey: null,
      header: "Action",
      cell: ({ row }) => (
        <span>
          <i onClick={() => handleDelete(row.original.id)}>
            <img
              className={st.iconMl}
              src={"/static/img/delete.png"}
              height={24}
              width={24}
            />
          </i>

          <i onClick={() => openWithEdit(row.original.id)}>
            <img
              className={st.iconMl}
              src={"/static/img/edit.png"}
              height={24}
              width={24}
            />
          </i>
        </span>
      ),
    },
  ];
};
