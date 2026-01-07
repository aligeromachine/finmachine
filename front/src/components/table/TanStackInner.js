import React, { useState, useMemo } from "react";
import {
  useReactTable,
  getCoreRowModel,
  getExpandedRowModel,
  getGroupedRowModel,
  getFilteredRowModel,
  getPaginationRowModel,
  flexRender,
} from "@tanstack/react-table";

// Данные с иерархической структурой
const defaultData = [
  {
    id: "dept-1",
    name: "Разработка",
    type: "department",
    budget: 5000000,
    employees: 15,
    children: [
      {
        id: "emp-1",
        name: "Иван Иванов",
        type: "employee",
        position: "Team Lead",
        salary: 250000,
        experience: 8,
        departmentId: "dept-1",
      },
      {
        id: "emp-2",
        name: "Мария Петрова",
        type: "employee",
        position: "Senior Developer",
        salary: 180000,
        experience: 6,
        departmentId: "dept-1",
      },
      {
        id: "emp-3",
        name: "Алексей Сидоров",
        type: "employee",
        position: "Middle Developer",
        salary: 120000,
        experience: 3,
        departmentId: "dept-1",
      },
    ],
  },
  {
    id: "dept-2",
    name: "Дизайн",
    type: "department",
    budget: 2000000,
    employees: 8,
    children: [
      {
        id: "emp-4",
        name: "Елена Васильева",
        type: "employee",
        position: "UI/UX Designer",
        salary: 150000,
        experience: 5,
        departmentId: "dept-2",
      },
      {
        id: "emp-5",
        name: "Дмитрий Козлов",
        type: "employee",
        position: "Graphic Designer",
        salary: 110000,
        experience: 4,
        departmentId: "dept-2",
      },
    ],
  },
  {
    id: "dept-3",
    name: "Маркетинг",
    type: "department",
    budget: 3000000,
    employees: 10,
    children: [
      {
        id: "emp-6",
        name: "Ольга Смирнова",
        type: "employee",
        position: "Marketing Manager",
        salary: 170000,
        experience: 7,
        departmentId: "dept-3",
      },
      {
        id: "emp-7",
        name: "Сергей Федоров",
        type: "employee",
        position: "SEO Specialist",
        salary: 130000,
        experience: 4,
        departmentId: "dept-3",
      },
      {
        id: "emp-8",
        name: "Анна Николаева",
        type: "employee",
        position: "Content Manager",
        salary: 90000,
        experience: 2,
        departmentId: "dept-3",
      },
    ],
  },
  {
    id: "dept-4",
    name: "Аналитика",
    type: "department",
    budget: 1500000,
    employees: 5,
    children: [
      {
        id: "emp-9",
        name: "Павел Орлов",
        type: "employee",
        position: "Data Analyst",
        salary: 160000,
        experience: 6,
        departmentId: "dept-4",
      },
      {
        id: "emp-10",
        name: "Татьяна Захарова",
        type: "employee",
        position: "BI Analyst",
        salary: 140000,
        experience: 5,
        departmentId: "dept-4",
      },
    ],
  },
];

// Компонент таблицы
const TreeTableWithAggregation = () => {
  const [data, setData] = useState(defaultData);
  const [expanded, setExpanded] = useState({});
  const [grouping, setGrouping] = useState([]);
  const [columnFilters, setColumnFilters] = useState([]);
  const [globalFilter, setGlobalFilter] = useState("");

  // Преобразование иерархических данных в плоский список
  const flatData = useMemo(() => {
    const flatten = (items) => {
      return items.flatMap((item) => {
        if (item.type === "department" && item.children) {
          return [item, ...flatten(item.children)];
        }
        return [item];
      });
    };
    return flatten(data);
  }, [data]);

  // Определение колонок
  const columns = useMemo(
    () => [
      {
        id: "expander",
        header: "",
        cell: ({ row }) => {
          if (row.getCanExpand()) {
            return (
              <button
                onClick={row.getToggleExpandedHandler()}
                className="w-6 h-6 flex items-center justify-center"
              >
                {row.getIsExpanded() ? "▼" : "▶"}
              </button>
            );
          }
          return null;
        },
      },
      {
        accessorKey: "name",
        header: "Название / Имя",
        cell: ({ row, getValue }) => {
          const indent = row.depth * 20;
          return (
            <div
              style={{ paddingLeft: `${indent}px` }}
              className="flex items-center"
            >
              {getValue()}
              {row.original.type === "department" && (
                <span className="ml-2 px-2 py-1 text-xs bg-blue-100 text-blue-800 rounded">
                  Отдел
                </span>
              )}
            </div>
          );
        },
      },
      {
        accessorKey: "type",
        header: "Тип",
        cell: (info) => (
          <span
            className={`px-2 py-1 text-xs rounded ${
              info.getValue() === "department"
                ? "bg-purple-100 text-purple-800"
                : "bg-green-100 text-green-800"
            }`}
          >
            {info.getValue() === "department" ? "Отдел" : "Сотрудник"}
          </span>
        ),
        enableGrouping: true,
      },
      {
        accessorKey: "position",
        header: "Должность",
        cell: (info) => info.getValue() || "-",
      },
      {
        accessorKey: "salary",
        header: "Зарплата",
        cell: (info) =>
          info.getValue()
            ? `${info.getValue().toLocaleString("ru-RU")} ₽`
            : "-",
        aggregationFn: "sum",
        aggregatedCell: ({ getValue }) =>
          `${getValue().toLocaleString("ru-RU")} ₽ (сумма)`,
      },
      {
        accessorKey: "budget",
        header: "Бюджет",
        cell: (info) =>
          info.getValue()
            ? `${info.getValue().toLocaleString("ru-RU")} ₽`
            : "-",
        aggregationFn: "sum",
        aggregatedCell: ({ getValue }) =>
          `${getValue().toLocaleString("ru-RU")} ₽ (сумма)`,
      },
      {
        accessorKey: "experience",
        header: "Опыт (лет)",
        cell: (info) => info.getValue() || "-",
        aggregationFn: "avg",
        aggregatedCell: ({ getValue }) =>
          `${Math.round(getValue() * 10) / 10} (среднее)`,
      },
      {
        accessorKey: "employees",
        header: "Сотрудников",
        cell: (info) => info.getValue() || "-",
        aggregationFn: "sum",
        aggregatedCell: ({ getValue }) => `${getValue()} (всего)`,
      },
    ],
    [],
  );

  // Создание таблицы
  const table = useReactTable({
    data: flatData,
    columns,
    state: {
      expanded,
      grouping,
      columnFilters,
      globalFilter,
    },
    onExpandedChange: setExpanded,
    onGroupingChange: setGrouping,
    onColumnFiltersChange: setColumnFilters,
    onGlobalFilterChange: setGlobalFilter,
    getSubRows: (row) => (row.type === "department" ? row.children : undefined),
    getCoreRowModel: getCoreRowModel(),
    getExpandedRowModel: getExpandedRowModel(),
    getGroupedRowModel: getGroupedRowModel(),
    getFilteredRowModel: getFilteredRowModel(),
    getPaginationRowModel: getPaginationRowModel(),
    initialState: {
      pagination: {
        pageSize: 10,
      },
    },
    enableGrouping: true,
    enableExpanding: true,
    filterFromLeafRows: true,
  });

  // Расчет агрегированных значений
  const calculateTotals = () => {
    const departments = data.filter((item) => item.type === "department");

    const totalBudget = departments.reduce((sum, dept) => sum + dept.budget, 0);
    const totalSalary = flatData
      .filter((item) => item.type === "employee")
      .reduce((sum, emp) => sum + emp.salary, 0);
    const totalEmployees = departments.reduce(
      (sum, dept) => sum + dept.employees,
      0,
    );
    const avgExperience = flatData
      .filter((item) => item.type === "employee")
      .reduce((sum, emp, _, arr) => sum + emp.experience / arr.length, 0);

    return { totalBudget, totalSalary, totalEmployees, avgExperience };
  };

  const totals = calculateTotals();

  return (
    <div className="p-4">
      <h2 className="text-2xl font-bold mb-6">
        Организационная структура с агрегацией
      </h2>

      {/* Панель управления */}
      <div className="mb-6 p-4 bg-gray-50 rounded-lg space-y-4">
        <div className="flex flex-wrap gap-4 items-center">
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Группировка:
            </label>
            <select
              className="px-3 py-2 border rounded-md"
              value={grouping[0] || ""}
              onChange={(e) =>
                setGrouping(e.target.value ? [e.target.value] : [])
              }
            >
              <option value="">Без группировки</option>
              <option value="type">По типу</option>
            </select>
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Поиск:
            </label>
            <input
              type="text"
              className="px-3 py-2 border rounded-md"
              placeholder="Поиск по всем полям..."
              value={globalFilter}
              onChange={(e) => setGlobalFilter(e.target.value)}
            />
          </div>

          <div className="flex gap-2">
            <button
              className="px-4 py-2 bg-blue-500 text-white rounded-md hover:bg-blue-600"
              onClick={() => table.toggleAllRowsExpanded(true)}
            >
              Раскрыть все
            </button>
            <button
              className="px-4 py-2 bg-gray-200 rounded-md hover:bg-gray-300"
              onClick={() => table.toggleAllRowsExpanded(false)}
            >
              Свернуть все
            </button>
          </div>
        </div>

        {/* Быстрые фильтры */}
        <div className="flex gap-2">
          <button
            className="px-3 py-1 text-sm bg-purple-100 text-purple-800 rounded-md"
            onClick={() => table.getColumn("type").setFilterValue("department")}
          >
            Только отделы
          </button>
          <button
            className="px-3 py-1 text-sm bg-green-100 text-green-800 rounded-md"
            onClick={() => table.getColumn("type").setFilterValue("employee")}
          >
            Только сотрудники
          </button>
          <button
            className="px-3 py-1 text-sm bg-gray-100 text-gray-800 rounded-md"
            onClick={() => table.resetColumnFilters()}
          >
            Сбросить фильтры
          </button>
        </div>
      </div>

      {/* Таблица */}
      <div className="overflow-x-auto border rounded-lg shadow">
        <table className="min-w-full divide-y divide-gray-200">
          <thead className="bg-gray-50">
            {table.getHeaderGroups().map((headerGroup) => (
              <tr key={headerGroup.id}>
                {headerGroup.headers.map((header) => (
                  <th
                    key={header.id}
                    className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
                    colSpan={header.colSpan}
                  >
                    {header.isPlaceholder ? null : (
                      <div>
                        {flexRender(
                          header.column.columnDef.header,
                          header.getContext(),
                        )}
                        {header.column.getCanGroup() && (
                          <button
                            className="ml-2 text-xs"
                            onClick={header.column.getToggleGroupingHandler()}
                          >
                            {header.column.getIsGrouped() ? "🚫" : "👥"}
                          </button>
                        )}
                      </div>
                    )}
                  </th>
                ))}
              </tr>
            ))}
          </thead>
          <tbody className="bg-white divide-y divide-gray-200">
            {table.getRowModel().rows.map((row) => {
              const isDepartment = row.original.type === "department";
              const isGrouped = row.getIsGrouped();

              return (
                <tr
                  key={row.id}
                  className={`
                    ${isDepartment ? "bg-blue-50" : "hover:bg-gray-50"}
                    ${isGrouped ? "font-bold" : ""}
                  `}
                >
                  {row.getVisibleCells().map((cell) => (
                    <td
                      key={cell.id}
                      className={`
                        px-6 py-4 whitespace-nowrap text-sm
                        ${cell.getIsAggregated() ? "text-orange-600 font-semibold" : ""}
                        ${cell.getIsGrouped() ? "text-purple-600" : ""}
                      `}
                    >
                      {flexRender(
                        cell.column.columnDef.cell,
                        cell.getContext(),
                      )}
                    </td>
                  ))}
                </tr>
              );
            })}
          </tbody>
        </table>
      </div>

      {/* Пагинация */}
      <div className="flex items-center justify-between mt-6 p-4 bg-gray-50 rounded-lg">
        <div className="flex items-center space-x-4">
          <button
            className="px-4 py-2 text-sm border rounded-md disabled:opacity-50 hover:bg-gray-100"
            onClick={() => table.previousPage()}
            disabled={!table.getCanPreviousPage()}
          >
            Назад
          </button>

          <span className="text-sm text-gray-700">
            Страница {table.getState().pagination.pageIndex + 1} из{" "}
            {table.getPageCount()}
          </span>

          <button
            className="px-4 py-2 text-sm border rounded-md disabled:opacity-50 hover:bg-gray-100"
            onClick={() => table.nextPage()}
            disabled={!table.getCanNextPage()}
          >
            Вперед
          </button>
        </div>

        <div className="flex items-center space-x-4">
          <select
            className="px-3 py-2 border rounded-md"
            value={table.getState().pagination.pageSize}
            onChange={(e) => table.setPageSize(Number(e.target.value))}
          >
            {[5, 10, 20, 50, 100].map((size) => (
              <option key={size} value={size}>
                {size} строк
              </option>
            ))}
          </select>

          <span className="text-sm text-gray-700">
            Показано {table.getRowModel().rows.length} из {flatData.length}{" "}
            строк
          </span>
        </div>
      </div>

      {/* Кнопки управления данными */}
      <div className="mt-4 flex gap-2">
        <button
          className="px-4 py-2 bg-green-500 text-white rounded-md hover:bg-green-600"
          onClick={() => {
            const newId = `emp-${Date.now()}`;
            const newEmployee = {
              id: newId,
              name: "Новый сотрудник",
              type: "employee",
              position: "Разработчик",
              salary: 100000,
              experience: 1,
              departmentId: "dept-1",
            };

            setData((prev) =>
              prev.map((dept) => {
                if (dept.id === "dept-1") {
                  return {
                    ...dept,
                    children: [...(dept.children || []), newEmployee],
                    employees: (dept.children || []).length + 1,
                  };
                }
                return dept;
              }),
            );
          }}
        >
          Добавить сотрудника
        </button>

        <button
          className="px-4 py-2 bg-red-500 text-white rounded-md hover:bg-red-600"
          onClick={() => {
            setData(defaultData);
            setExpanded({});
            setGrouping([]);
            setColumnFilters([]);
            setGlobalFilter("");
          }}
        >
          Сбросить данные
        </button>
      </div>
    </div>
  );
};

export default TreeTableWithAggregation;
