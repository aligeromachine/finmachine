import React from "react";

export const routes = [
  { path: "/", exact: true, name: "Home" },
  {
    path: "/dashboard",
    name: "Dashboard",
    element: React.lazy(() => import("../../views/dashboard/Dashboard")),
  },
  {
    path: "/buy",
    name: "Buy",
    element: React.lazy(() => import("../../views/buy/Buy")),
  },
  {
    path: "/cards",
    name: "Cards",
    element: React.lazy(() => import("../../views/cards/Cards")),
  },
  {
    path: "/shop",
    name: "Shop",
    element: React.lazy(() => import("../../views/shop/Shop")),
  },
  {
    path: "/products",
    name: "Products",
    element: React.lazy(() => import("../../views/products/Products")),
  },
  {
    path: "/profit",
    name: "Profit",
    element: React.lazy(() => import("../../views/profit/Profit")),
  },
];
