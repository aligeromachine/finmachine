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
