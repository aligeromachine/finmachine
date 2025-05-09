import React from "react";

function lazyNamedImport(exportName = "default") {
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
    element: lazyNamedImport("Dashboard"),
  },
  {
    path: "/buy",
    name: "Buy",
    element: lazyNamedImport("Buy"),
  },
  {
    path: "/cards",
    name: "Cards",
    element: lazyNamedImport("Cards"),
  },
  {
    path: "/shop",
    name: "Shop",
    element: lazyNamedImport("Shop"),
  },
  {
    path: "/products",
    name: "Products",
    element: lazyNamedImport("Prod"),
  },
  {
    path: "/profit",
    name: "Profit",
    element: lazyNamedImport("Profit"),
  },
];
