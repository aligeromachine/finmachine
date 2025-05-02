import React from "react";
import { CToast, CToastBody, CToastClose } from "@coreui/react";

export const ToastLive = ({ title, message }) => {
  return (
    <CToast visible={true} className="align-items-center">
      <div className="d-flex">
        <CToastBody>Hello, world! This is a toast message.</CToastBody>
        <CToastClose className="me-2 m-auto" />
      </div>
    </CToast>
  );
};
