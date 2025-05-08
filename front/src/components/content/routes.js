import React from "react";

const Dashboard = React.lazy(() => import("../../views/dashboard/Dashboard"));

const Buy = React.lazy(() => import("../../views/buy/Buy"));
const Cards = React.lazy(() => import("../../views/cards/Cards"));
const Shop = React.lazy(() => import("../../views/shop/Shop"));
const Products = React.lazy(() => import("../../views/products/Products"));
const Profit = React.lazy(() => import("../../views/profit/Profit"));

export const routes = [
  { path: "/", exact: true, name: "Home" },
  { path: "/dashboard", name: "Dashboard", element: Dashboard },
  { path: "/buy", name: "Buy", element: Buy },
  { path: "/cards", name: "Cards", element: Cards },
  { path: "/shop", name: "Shop", element: Shop },
  { path: "/products", name: "Products", element: Products },
  { path: "/profit", name: "Profit", element: Profit },
];
