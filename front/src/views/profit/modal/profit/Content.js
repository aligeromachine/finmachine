import {
  CButton,
  CModal,
  CModalBody,
  CModalFooter,
  CModalHeader,
  CModalTitle,
  CFormInput,
  CFormSelect,
  CCol,
  CForm,
} from "@coreui/react";
import { RedCAlert } from "../../../../components/redflag/RedCAlert";
import { RedLable } from "../../../../components/redflag/RedLable";

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
        <CModalTitle>Source Data</CModalTitle>
      </CModalHeader>
      <CModalBody>
        <CForm className="row g-3">
          <CCol xs={12}>
            <CFormInput
              label="Title"
              placeholder="Zarplata"
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
          <CCol xs={12}>
            <CFormSelect
              label="Source"
              aria-label="Default select example"
              options={[
                { label: "Open this select menu" },
                { label: "One", value: "1" },
                { label: "Two", value: "2" },
                { label: "Three", value: "3", disabled: true },
              ]}
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
