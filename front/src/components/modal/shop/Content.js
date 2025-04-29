import React from "react";
import { CFormInput, CInputGroup, CInputGroupText } from "@coreui/react";

export const ContentShop = () => {
  return (
    <>
      <CInputGroup size="lg" className="mb-3">
        <CInputGroupText id="shop_title">Title</CInputGroupText>
        <CFormInput
          aria-label="Sizing example input"
          aria-describedby="inputGroup-sizing-lg"
        />
      </CInputGroup>
      <CInputGroup size="lg" className="mb-3">
        <CInputGroupText id="shop_address">Address</CInputGroupText>
        <CFormInput
          aria-label="Sizing example input"
          aria-describedby="inputGroup-sizing-lg"
        />
      </CInputGroup>
    </>
  );
};
