import React from "react";
import CIcon from "@coreui/icons-react";
import {
  cilBell,
  cilCalculator,
  cilChartPie,
  cilCursor,
  cilDescription,
  cilDrop,
  cilExternalLink,
  cilNotes,
  cilPencil,
  cilPuzzle,
  cilRecycle,
  cilSpeedometer,
  cilStar,
  cibBlogger,
  cilAppsSettings,
} from "@coreui/icons";
import { CNavItem, CNavTitle } from "@coreui/react";

const _nav = [
  {
    component: CNavItem,
    name: "Dashboard",
    to: "/dashboard",
    icon: <CIcon icon={cilSpeedometer} customClassName="nav-icon" />,
  },
  {
    component: CNavTitle,
    name: "Components",
  },
  {
    component: CNavItem,
    name: "Buy",
    to: "/buy",
    icon: <CIcon icon={cilRecycle} customClassName="nav-icon" />,
  },
  {
    component: CNavItem,
    name: "Products",
    to: "/products",
    icon: <CIcon icon={cilDescription} customClassName="nav-icon" />,
  },
  {
    component: CNavItem,
    name: "Profit",
    to: "/profit",
    icon: <CIcon icon={cilCalculator} customClassName="nav-icon" />,
  },
  {
    component: CNavItem,
    name: "Cards",
    to: "/cards",
    icon: <CIcon icon={cilNotes} customClassName="nav-icon" />,
  },
  {
    component: CNavItem,
    name: "Shop",
    to: "/shop",
    icon: <CIcon icon={cilPuzzle} customClassName="nav-icon" />,
  },
  {
    component: CNavItem,
    name: "Logger",
    to: "/logger",
    icon: <CIcon icon={cilBell} customClassName="nav-icon" />,
  },
  {
    component: CNavItem,
    name: "Config",
    to: "/config",
    icon: <CIcon icon={cilAppsSettings} customClassName="nav-icon" />,
  },
];

export default _nav;
