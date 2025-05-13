import React from "react";
import { handleDelete } from "../../../components/action/Action";
import {
  deleteProfitRow,
  getProfitRow,
} from "../../../services/profit/request";
import st from "./row.module.css";

export const columnsTbl = (openModal) => {
  const openWithEdit = async (id) => {
    await getProfitRow(id);
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
      accessorKey: "amount",
      header: "Amount",
    },
    {
      accessorKey: "source",
      header: "Source",
    },
    {
      accessorKey: null,
      header: "Action",
      cell: ({ row }) => (
        <span>
          <i onClick={() => handleDelete(row.original.id, deleteProfitRow)}>
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
