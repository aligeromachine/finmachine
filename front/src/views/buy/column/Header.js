import React from "react";
import { handleDeleteRow } from "../../../components/action/Action";
import { deleteBuyRow, getBuyRow } from "../../../services/buys/request";
import st from "./row.module.css";

export const columnsTbl = (openModal) => {
  const openWithEdit = async (id) => {
    await getBuyRow(id);
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
      accessorKey: "shop",
      header: "Shop",
    },
    {
      accessorKey: "cat",
      header: "Catalog",
    },
    {
      accessorKey: "prod",
      header: "Prod",
    },
    {
      accessorKey: "amount",
      header: "Amount",
    },
    {
      accessorKey: "title",
      header: "Title",
    },
    {
      accessorKey: null,
      header: "Action",
      cell: ({ row }) => (
        <span>
          <i onClick={() => handleDeleteRow(row.original.id, deleteBuyRow)}>
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
