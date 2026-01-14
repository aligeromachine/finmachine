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
import { RedCAlert } from "../../../../components/elems/RedCAlert";
import { RedLable } from "../../../../components/elems/RedCAlert";
import { getSourceOptions } from "../../../../services/source/query";
import { AsyncFormSelect } from "../../../../components/form/Select";
import { DatePicElem } from "../../../../components/datetimepiker/BigDatepicker";

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
    <CModal size="lg" visible={visible} onClose={onClose}>
      <CModalHeader>
        <CModalTitle>Source Data</CModalTitle>
      </CModalHeader>
      <CModalBody>
        <CForm className="row g-3">
          <DatePicElem
            onChange={onChange}
            value={formData.created}
            name={"created"}
          />
          <CCol xs={12}>
            <AsyncFormSelect
              label={"Source"}
              onChange={onChange}
              value={formData.source || ""}
              name={"source"}
              request={getSourceOptions}
            />
            <RedLable title={validate.title} />
          </CCol>
          <CCol xs={12}>
            <CFormInput
              label="Title"
              placeholder="April"
              onChange={onChange}
              value={formData.title || ""}
              name={"title"}
            />
            <RedLable title={validate.title} />
          </CCol>
          <CCol xs={12}>
            <CFormInput
              label="Amount"
              placeholder="235456.2"
              onChange={onChange}
              value={formData.amount || ""}
              name={"amount"}
            />
            <RedLable title={validate.amount} />
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
