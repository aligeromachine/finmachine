import React from "react";
import { CAlert, CFormLabel } from "@coreui/react";

export const RedCAlert = ({ title }) => {
  return <>{title && <CAlert color="danger">{title}</CAlert>}</>;
};

export const RedLable = ({ title }) => {
  return (
    <>{title && <CFormLabel className="text-danger">{title}</CFormLabel>}</>
  );
};
