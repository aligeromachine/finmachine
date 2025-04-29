import React from "react";
import { CFormLabel } from "@coreui/react";

export const RedLable = ({ title }) => {
  return (
    <>{title && <CFormLabel className="text-danger">{title}</CFormLabel>}</>
  );
};
