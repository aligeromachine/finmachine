import React, { useState, useMemo } from 'react';
import { useReactTable, getCoreRowModel, getPaginationRowModel, flexRender } from '@tanstack/react-table';

// Пример данных
const defaultData = [
    { id: 1, name: 'Алексей', email: 'alex@example.com', age: 28 },
    { id: 2, name: 'Мария', email: 'maria@example.com', age: 32 },
    { id: 3, name: 'Иван', email: 'ivan@example.com', age: 25 },
    { id: 4, name: 'Ольга', email: 'olga@example.com', age: 29 },
    { id: 5, name: 'Дмитрий', email: 'dmitry@example.com', age: 35 },
    { id: 6, name: 'Елена', email: 'elena@example.com', age: 31 },
    { id: 7, name: 'Сергей', email: 'sergey@example.com', age: 27 },
    { id: 8, name: 'Анна', email: 'anna@example.com', age: 33 },
];

// Компонент таблицы
function UserTable() {
    const [data] = useState(() => [...defaultData]);
    const [pagination, setPagination] = useState({
        pageIndex: 0,
        pageSize: 5,
    });

    // Определение колонок
    const columns = useMemo(
        () => [
            {
                accessorKey: 'id',
                header: 'ID',
                size: 60,
            },
            {
                accessorKey: 'name',
                header: 'Имя',
                cell: info => info.getValue(),
            },
            {
                accessorKey: 'email',
                header: 'Email',
            },
            {
                accessorKey: 'age',
                header: 'Возраст',
            },
        ],
        []
    );

    // Создание таблицы
    const table = useReactTable({
        data,
        columns,
        state: {
            pagination,
        },
        onPaginationChange: setPagination,
        getCoreRowModel: getCoreRowModel(),
        getPaginationRowModel: getPaginationRowModel(),
        debugTable: true,
    });

    return (
        <div className="p-2">
            <table className="table">
                <thead>
                    {table.getHeaderGroups().map(headerGroup => (
                        <tr key={headerGroup.id}>
                            {headerGroup.headers.map(header => (
                                <th key={header.id} colSpan={header.colSpan}>
                                    {header.isPlaceholder ? null : flexRender(header.column.columnDef.header, header.getContext())}
                                </th>
                            ))}
                        </tr>
                    ))}
                </thead>
                <tbody>
                    {table.getRowModel().rows.map(row => (
                        <tr key={row.id}>
                            {row.getVisibleCells().map(cell => (
                                <td key={cell.id}>{flexRender(cell.column.columnDef.cell, cell.getContext())}</td>
                            ))}
                        </tr>
                    ))}
                </tbody>
            </table>

            {/* Пагинация */}
            <div className="pagination">
                <button className="border rounded p-1" onClick={() => table.firstPage()} disabled={!table.getCanPreviousPage()}>
                    {'<<'}
                </button>
                <button className="border rounded p-1" onClick={() => table.previousPage()} disabled={!table.getCanPreviousPage()}>
                    {'<'}
                </button>
                <button className="border rounded p-1" onClick={() => table.nextPage()} disabled={!table.getCanNextPage()}>
                    {'>'}
                </button>
                <button className="border rounded p-1" onClick={() => table.lastPage()} disabled={!table.getCanNextPage()}>
                    {'>>'}
                </button>

                <span className="flex items-center gap-1">
                    <div>Страница</div>
                    <strong>
                        {table.getState().pagination.pageIndex + 1} из {table.getPageCount()}
                    </strong>
                </span>

                <span className="flex items-center gap-1">
                    | Перейти к странице:
                    <input
                        type="number"
                        defaultValue={table.getState().pagination.pageIndex + 1}
                        onChange={e => {
                            const page = e.target.value ? Number(e.target.value) - 1 : 0;
                            table.setPageIndex(page);
                        }}
                        className="border p-1 rounded w-16"
                    />
                </span>

                <select
                    value={table.getState().pagination.pageSize}
                    onChange={e => {
                        table.setPageSize(Number(e.target.value));
                    }}
                >
                    {[5, 10, 20, 30, 40, 50].map(pageSize => (
                        <option key={pageSize} value={pageSize}>
                            Показать {pageSize}
                        </option>
                    ))}
                </select>
            </div>

            <div>{table.getRowModel().rows.length} строк</div>
        </div>
    );
}

export default UserTable;
