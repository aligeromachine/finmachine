import React from "react";
import { handleDelete } from "../../../components/action/Action";
import { deleteProdRow, getProdRow } from "../../../services/products/request";
import st from "./row.module.css";

export const columnsTbl = (openModal) => {
  const openWithEdit = async (id) => {
    await getProdRow(id);
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
      accessorKey: "catalog",
      header: "Catalog",
    },
    {
      accessorKey: null,
      header: "Action",
      cell: ({ row }) => (
        <span>
          <i onClick={() => handleDelete(row.original.id, deleteProdRow)}>
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
