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
import { RedCAlert } from "../../../components/elems/RedCAlert";
import { RedLable } from "../../../components/elems/RedCAlert";

export const CardsContent = ({
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
        <CModalTitle>Cards Data</CModalTitle>
      </CModalHeader>
      <CModalBody>
        <CForm className="row g-3">
          <CCol xs={12}>
            <CFormInput
              label="Title"
              placeholder="Vtb"
              onChange={onChange}
              value={formData.title || ""}
              name={"title"}
            />
            <RedLable title={validate.title} />
          </CCol>
          <CCol xs={12}>
            <CFormInput
              label="Amount"
              placeholder="100.00"
              onChange={onChange}
              value={formData.amount || ""}
              name={"amount"}
            />
            <RedLable title={validate.amount} />
          </CCol>
          <CCol xs={12}>
            <CFormInput
              label="Number"
              placeholder="2200 1000 4000 5000"
              onChange={onChange}
              value={formData.number || ""}
              name={"number"}
            />
            <RedLable title={validate.number} />
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
