import React from "react";
import { CFormInput, CCol, CForm } from "@coreui/react";
import { RedLable } from "../../../components/redflag/RedLable";

export const ContentShop = ({ onChange, formData, validate }) => {
  return (
    <CForm className="row g-3">
      <CCol xs={12}>
        <CFormInput
          id="input_title"
          label="Title"
          placeholder="Magazine"
          onChange={onChange}
          value={formData.title || ""}
          name={"title"}
        />
        <RedLable title={validate.title} />
      </CCol>
      <CCol xs={12}>
        <CFormInput
          id="input_address"
          label="Address"
          placeholder="Moscow City, Pavlova st.19"
          onChange={onChange}
          value={formData.address || ""}
          name={"address"}
        />
        <RedLable title={validate.address} />
      </CCol>
    </CForm>
  );
};
