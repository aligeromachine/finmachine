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
import { DatePicElem } from "../../../../components/datetimepiker/BigDatepicker";

export const SourceContent = ({
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
        <CModalTitle>Catalog Data</CModalTitle>
      </CModalHeader>
      <CModalBody>
        <CForm className="row g-3">
          <DatePicElem
            onChange={onChange}
            value={formData.created || new Date()}
            name={"created"}
          />
          <CCol xs={12}>
            <CFormInput
              label="Title"
              placeholder="Kolbasnye"
              onChange={onChange}
              value={formData.title || ""}
              name={"title"}
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
