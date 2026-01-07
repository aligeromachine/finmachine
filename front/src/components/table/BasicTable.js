// src/BasicTable.jsx
import { useState } from "react";
import {
  useReactTable,
  getCoreRowModel,
  getFilteredRowModel,
  getSortedRowModel,
  getPaginationRowModel,
  flexRender,
} from "@tanstack/react-table";
import { rankItem } from "@tanstack/match-sorter-utils";
import "./styles.css";

import {
  CButton,
  CDropdown,
  CDropdownItem,
  CDropdownMenu,
  CDropdownToggle,
} from "@coreui/react";
import { right } from "@popperjs/core";
import { CPagination, CPaginationItem } from "@coreui/react";

// Custom fuzzy filter function for approximate matches
const fuzzyFilter = (row, columnId, value, addMeta) => {
  // Rank the item based on the search value
  const itemRank = rankItem(row.getValue(columnId), value);

  // Store ranking metadata for sorting
  addMeta({
    itemRank,
  });

  // Return whether the item passes the filter
  return itemRank.passed;
};
const totalPages = 100;

const totalCount = 100000;

export function BasicTable({ data, columns }) {
  // Define states for global filtering and sorting
  const [globalFilter, setGlobalFilter] = useState("");
  const [sorting, setSorting] = useState([]);
  // Состояние пагинации
  const [pagination, setPagination] = useState({
    pageIndex: 0, // начинается с 0
    pageSize: 10,
  });

  // Create the table instance with necessary configurations
  const table = useReactTable({
    data,
    columns,
    filterFns: {
      fuzzy: fuzzyFilter, // Register the fuzzy filter for global use
    },
    state: {
      globalFilter, // Manage the global filter state
      sorting, // Manage the sorting state
      pagination,
    },
    onGlobalFilterChange: setGlobalFilter, // Update the global filter state when it changes
    globalFilterFn: "fuzzy", // Specify the fuzzy filter function for global filtering
    onSortingChange: setSorting, // Update the sorting state when sorting changes
    getCoreRowModel: getCoreRowModel(), // Core row model for displaying rows
    getFilteredRowModel: getFilteredRowModel(), // Enable filtering functionality
    getSortedRowModel: getSortedRowModel(), // Enable sorting functionality
    onPaginationChange: setPagination,
    getPaginationRowModel: getPaginationRowModel(),
    pageCount: totalPages,
    manualPagination: true, // Важно: ручное управление пагинацией
  });

  return (
    <div>
      <input
        type="text"
        value={globalFilter}
        onChange={(e) => setGlobalFilter(e.target.value)} // Update filter value on user input
        placeholder="Search..."
        style={{ marginBottom: "10px", padding: "5px", width: "100%" }}
      />
      <table>
        <thead>
          {table.getHeaderGroups().map((headerGroup) => (
            <tr key={headerGroup.id}>
              {headerGroup.headers.map((header) => (
                <th
                  key={header.id}
                  colSpan={header.colSpan}
                  onClick={header.column.getToggleSortingHandler()} // Add sorting on column headers
                  style={{
                    cursor: header.column.getCanSort() ? "pointer" : "default", // Indicate sortable columns with a pointer cursor
                  }}
                  className="text-center"
                >
                  {header.isPlaceholder
                    ? null
                    : flexRender(
                        header.column.columnDef.header, // Render the header content
                        header.getContext(),
                      )}
                  {{
                    asc: " 🔼", // Display ascending sort indicator
                    desc: " 🔽", // Display descending sort indicator
                  }[header.column.getIsSorted()] ?? null}
                </th>
              ))}
            </tr>
          ))}
        </thead>
        <tbody>
          {table.getRowModel().rows.map((row) => (
            <tr key={row.id}>
              {row.getVisibleCells().map((cell) => (
                <td key={cell.id} className="text-center">
                  {flexRender(cell.column.columnDef.cell, cell.getContext())}
                </td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>

      {/* Пагинация */}
      <div className="flex items-center justify-between border-t border-gray-200">
        {/* Информация о странице */}
        <div className="text-sm text-gray-700">
          <span className="font-medium">
            Страница {table.getState().pagination.pageIndex + 1}
          </span>{" "}
          из <span className="font-medium">{totalPages}</span>
        </div>

        {/* Элементы управления пагинацией */}
        <div className="flex items-center">
          <CButton
            onClick={() => table.firstPage()}
            disabled={!table.getCanPreviousPage()}
            color="primary"
            className="rounded-0"
          >
            Первая
          </CButton>
          <CButton
            onClick={() => table.previousPage()}
            disabled={!table.getCanPreviousPage()}
            color="secondary"
            className="rounded-0"
          >
            Назад
          </CButton>

          <CButton
            onClick={() => table.nextPage()}
            disabled={!table.getCanNextPage()}
            color="secondary"
            className="rounded-0"
          >
            Вперед
          </CButton>
          <CButton
            color="success"
            className="rounded-0"
            onClick={() => table.lastPage()}
            disabled={!table.getCanNextPage()}
          >
            Последняя
          </CButton>
        </div>
      </div>
    </div>
  );
}
