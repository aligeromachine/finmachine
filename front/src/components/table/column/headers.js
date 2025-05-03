import { handleDelete } from "./tableAction";
import st from "./row.module.css";

export const columnsBuy = [
  {
    accessorKey: "id", // Accessor key for the "name" field from data object
    header: "Id", // Column header
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
    accessorKey: "prod",
    header: "Prod",
  },
  {
    accessorKey: "amount",
    header: "Price",
  },
  {
    accessorKey: "title",
    header: "Title",
  },
  {
    accessorKey: null,
    header: "Action",
  },
];

export const columnsCards = [
  {
    accessorKey: "id", // Accessor key for the "name" field from data object
    header: "Id", // Column header
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
    accessorKey: "number",
    header: "Number",
  },
  {
    accessorKey: "amount",
    header: "Price",
  },
  {
    accessorKey: null,
    header: "Action",
  },
];

export const columnsShop = [
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

        <i onClick={() => handleDelete(row.original.id)}>
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

export const columnsProfit = [
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
    accessorKey: "sources",
    header: "Sources",
  },
  {
    accessorKey: "title",
    header: "Title",
  },
  {
    accessorKey: null,
    header: "Action",
  },
];

export const columnsSource = [
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
    accessorKey: null,
    header: "Action",
  },
];

export const columnsProducts = [
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
    accessorKey: "cats",
    header: "Catalog",
  },
  {
    accessorKey: "title",
    header: "Title",
  },
  {
    accessorKey: null,
    header: "Action",
  },
];

export const columnsCatalog = [
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
    accessorKey: null,
    header: "Action",
  },
];
