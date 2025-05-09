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
import { RedCAlert } from "../../../components/redflag/RedCAlert";
import { RedLable } from "../../../components/redflag/RedLable";

export const CardsContent = ({
  visible,
  onClose,
  formData,
  onChange,
  validate,
  respoErr,
  onAdd,
}) => {
  return (
    <CModal backdrop="static" size="lg" visible={visible} onClose={onClose}>
      <CModalHeader>
        <CModalTitle id="header_cards_modal">Cards Data</CModalTitle>
      </CModalHeader>
      <CModalBody>
        <CForm className="row g-3">
          <CCol xs={12}>
            <CFormInput
              id="cards_title"
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
              id="cards_amount"
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
              id="cards_number"
              label="Number"
              placeholder="2200 1000 4000 5000"
              onChange={onChange}
              value={formData.number || ""}
              name={"number"}
            />
            <RedLable title={validate.number} />
          </CCol>
        </CForm>
        <RedCAlert title={respoErr} />
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
