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
      <div className="bg-white px-4 py-3 flex items-center justify-between border-t border-gray-200">
        <div className="flex-1 flex justify-between items-center flex-wrap gap-2">
          {/* Информация о странице */}
          <div className="text-sm text-gray-700">
            Показано <span className="font-medium">{data.length}</span> из{" "}
            <span className="font-medium">{totalCount}</span> записей
          </div>

          {/* Элементы управления пагинацией */}
          <div className="flex items-center space-x-2">
            <button
              onClick={() => table.firstPage()}
              disabled={!table.getCanPreviousPage()}
              className="px-3 py-1 border rounded text-sm disabled:opacity-50 disabled:cursor-not-allowed hover:bg-gray-50"
            >
              Первая
            </button>
            <button
              onClick={() => table.previousPage()}
              disabled={!table.getCanPreviousPage()}
              className="px-3 py-1 border rounded text-sm disabled:opacity-50 disabled:cursor-not-allowed hover:bg-gray-50"
            >
              Назад
            </button>

            <span className="text-sm text-gray-700 mx-2">
              Страница{" "}
              <span className="font-medium">
                {table.getState().pagination.pageIndex + 1}
              </span>{" "}
              из <span className="font-medium">{totalPages}</span>
            </span>

            <button
              onClick={() => table.nextPage()}
              disabled={!table.getCanNextPage()}
              className="px-3 py-1 border rounded text-sm disabled:opacity-50 disabled:cursor-not-allowed hover:bg-gray-50"
            >
              Вперед
            </button>
            <CButton
              color="secondary"
              variant="outline"
              onClick={() => table.lastPage()}
              disabled={!table.getCanNextPage()}
            >
              Последняя
            </CButton>

            {/* Выбор размера страницы */}

            <select
              value={table.getState().pagination.pageSize}
              onChange={(e) => {
                table.setPageSize(Number(e.target.value));
              }}
              className="border border-gray-300 rounded px-3 py-1 text-sm disabled:opacity-50"
            >
              {[5, 10, 20, 50].map((pageSize) => (
                <option key={pageSize} value={pageSize}>
                  {pageSize}
                </option>
              ))}
            </select>
          </div>
        </div>
      </div>
    </div>
  );
}
