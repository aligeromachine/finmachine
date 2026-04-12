import React, { useState, useEffect, useMemo } from 'react';
import {
  useReactTable,
  getCoreRowModel,
  getPaginationRowModel,
  flexRender,
} from '@tanstack/react-table';

// Тип для пользователя
const User = {
  id: number;
  name: string;
  email: string;
  phone: string;
  website: string;
};

// Тип для ответа от API
interface ApiResponse {
  users: User[];
  total: number;
  page: number;
  totalPages: number;
}

function ServerSideTable() {
  const [data, setData] = useState<User[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [totalPages, setTotalPages] = useState(0);
  const [totalCount, setTotalCount] = useState(0);
  
  // Состояние пагинации
  const [pagination, setPagination] = useState({
    pageIndex: 0, // начинается с 0
    pageSize: 10,
  });

  // Функция загрузки данных с сервера
  const fetchData = async (pageIndex: number, pageSize: number) => {
    setLoading(true);
    setError(null);
    
    try {
      // Имитация API запроса
      const response = await fetch(
        `https://jsonplaceholder.typicode.com/users?_page=${pageIndex + 1}&_limit=${pageSize}`
      );
      
      if (!response.ok) {
        throw new Error('Ошибка загрузки данных');
      }
      
      const users = await response.json();
      
      // Получаем общее количество из заголовков
      const totalCount = parseInt(response.headers.get('x-total-count') || '0');
      
      setData(users);
      setTotalCount(totalCount);
      setTotalPages(Math.ceil(totalCount / pageSize));
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Произошла ошибка');
    } finally {
      setLoading(false);
    }
  };

  // Загрузка данных при изменении пагинации
  useEffect(() => {
    fetchData(pagination.pageIndex, pagination.pageSize);
  }, [pagination.pageIndex, pagination.pageSize]);

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
        cell: info => <strong>{info.getValue()}</strong>,
      },
      {
        accessorKey: 'email',
        header: 'Email',
      },
      {
        accessorKey: 'phone',
        header: 'Телефон',
      },
      {
        accessorKey: 'website',
        header: 'Вебсайт',
        cell: info => (
          <a 
            href={`https://${info.getValue()}`} 
            target="_blank" 
            rel="noopener noreferrer"
            className="text-blue-600 hover:underline"
          >
            {info.getValue()}
          </a>
        ),
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
    pageCount: totalPages,
    manualPagination: true, // Важно: ручное управление пагинацией
  });

  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold mb-4">Пользователи (серверная пагинация)</h1>
      
      {error && (
        <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4">
          {error}
        </div>
      )}

      <div className="bg-white shadow-md rounded-lg overflow-hidden">
        <div className="overflow-x-auto">
          <table className="min-w-full divide-y divide-gray-200">
            <thead className="bg-gray-50">
              {table.getHeaderGroups().map(headerGroup => (
                <tr key={headerGroup.id}>
                  {headerGroup.headers.map(header => (
                    <th
                      key={header.id}
                      className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
                    >
                      {header.isPlaceholder
                        ? null
                        : flexRender(
                            header.column.columnDef.header,
                            header.getContext()
                          )}
                    </th>
                  ))}
                </tr>
              ))}
            </thead>
            <tbody className="bg-white divide-y divide-gray-200">
              {loading ? (
                // Состояние загрузки
                <tr>
                  <td colSpan={columns.length} className="px-6 py-4 text-center">
                    <div className="flex justify-center items-center">
                      <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-blue-600"></div>
                      <span className="ml-2">Загрузка данных...</span>
                    </div>
                  </td>
                </tr>
              ) : (
                // Данные
                table.getRowModel().rows.map(row => (
                  <tr key={row.id} className="hover:bg-gray-50">
                    {row.getVisibleCells().map(cell => (
                      <td key={cell.id} className="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                        {flexRender(cell.column.columnDef.cell, cell.getContext())}
                      </td>
                    ))}
                  </tr>
                ))
              )}
            </tbody>
          </table>
        </div>

        {/* Пагинация */}
        <div className="bg-white px-4 py-3 flex items-center justify-between border-t border-gray-200">
          <div className="flex-1 flex justify-between items-center flex-wrap gap-2">
            {/* Информация о странице */}
            <div className="text-sm text-gray-700">
              Показано <span className="font-medium">{data.length}</span> из{' '}
              <span className="font-medium">{totalCount}</span> записей
            </div>

            {/* Элементы управления пагинацией */}
            <div className="flex items-center space-x-2">
              <button
                onClick={() => table.firstPage()}
                disabled={!table.getCanPreviousPage() || loading}
                className="px-3 py-1 border rounded text-sm disabled:opacity-50 disabled:cursor-not-allowed hover:bg-gray-50"
              >
                Первая
              </button>
              <button
                onClick={() => table.previousPage()}
                disabled={!table.getCanPreviousPage() || loading}
                className="px-3 py-1 border rounded text-sm disabled:opacity-50 disabled:cursor-not-allowed hover:bg-gray-50"
              >
                Назад
              </button>
              
              <span className="text-sm text-gray-700 mx-2">
                Страница <span className="font-medium">{table.getState().pagination.pageIndex + 1}</span>{' '}
                из <span className="font-medium">{totalPages}</span>
              </span>
              
              <button
                onClick={() => table.nextPage()}
                disabled={!table.getCanNextPage() || loading}
                className="px-3 py-1 border rounded text-sm disabled:opacity-50 disabled:cursor-not-allowed hover:bg-gray-50"
              >
                Вперед
              </button>
              <button
                onClick={() => table.lastPage()}
                disabled={!table.getCanNextPage() || loading}
                className="px-3 py-1 border rounded text-sm disabled:opacity-50 disabled:cursor-not-allowed hover:bg-gray-50"
              >
                Последняя
              </button>
            </div>

            {/* Выбор размера страницы */}
            <select
              value={table.getState().pagination.pageSize}
              onChange={e => {
                table.setPageSize(Number(e.target.value));
              }}
              disabled={loading}
              className="border border-gray-300 rounded px-2 py-1 text-sm disabled:opacity-50"
            >
              {[5, 10, 20, 50].map(pageSize => (
                <option key={pageSize} value={pageSize}>
                  {pageSize} на странице
                </option>
              ))}
            </select>
          </div>
        </div>
      </div>
    </div>
  );
}

export default ServerSideTable;