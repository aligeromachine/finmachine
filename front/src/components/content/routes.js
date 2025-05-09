import React from "react";

function lazyImport(exportName) {
  return React.lazy(async () => {
    const module = await (() => import("../../views/"))();
    return { default: module[exportName] };
  });
}

export const routes = [
  { path: "/", exact: true, name: "Home" },
  {
    path: "/dashboard",
    name: "Dashboard",
    element: lazyImport("Dashboard"),
  },
  {
    path: "/buy",
    name: "Buy",
    element: lazyImport("Buy"),
  },
  {
    path: "/cards",
    name: "Cards",
    element: lazyImport("Cards"),
  },
  {
    path: "/shop",
    name: "Shop",
    element: lazyImport("Shop"),
  },
  {
    path: "/products",
    name: "Products",
    element: lazyImport("Prod"),
  },
  {
    path: "/profit",
    name: "Profit",
    element: lazyImport("Profit"),
  },
];
