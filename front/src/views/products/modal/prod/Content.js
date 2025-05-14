import React from "react";
import {
  CButton,
  CModal,
  CModalBody,
  CModalFooter,
  CModalHeader,
  CModalTitle,
  CFormInput,
  CCol,
  CForm,
} from "@coreui/react";
import { RedCAlert } from "../../../../components/redflag/RedCAlert";
import { RedLable } from "../../../../components/redflag/RedLable";
import { getCatalogOptions } from "../../../../services/catalog/query";
import { AsyncFormSelect } from "../../../../components/form/Select";

export const ProfitContent = ({
  visible,
  onClose,
  formData,
  onChange,
  validate,
  repErr,
  onAdd,
}) => {
  return (
    <CModal backdrop="static" size="lg" visible={visible} onClose={onClose}>
      <CModalHeader>
        <CModalTitle>Products Data</CModalTitle>
      </CModalHeader>
      <CModalBody>
        <CForm className="row g-3">
          <CCol xs={12}>
            <CFormInput
              label="Title"
              placeholder="Doctorskaya"
              onChange={onChange}
              value={formData.title || ""}
              name={"title"}
            />
            <RedLable title={validate.title} />
          </CCol>
          <CCol xs={12}>
            <AsyncFormSelect
              onChange={onChange}
              value={formData.catalog || ""}
              name={"catalog"}
              request={getCatalogOptions}
            />
            <RedLable title={validate.title} />
          </CCol>
        </CForm>
        <RedCAlert title={repErr} />
      </CModalBody>
      <CModalFooter>
        <CButton color="secondary" onClick={onClose}>
          Close
        </CButton>
        <CButton color="primary" onClick={onAdd}>
          Save changes
        </CButton>
      </CModalFooter>
    </CModal>
  );
};
