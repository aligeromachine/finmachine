import React from "react";
import { CAlert } from "@coreui/react";

export const RedCAlert = ({ title }) => {
  return <>{title && <CAlert color="danger">{title}</CAlert>}</>;
};
