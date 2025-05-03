import {
  CButton,
  CModal,
  CModalBody,
  CModalFooter,
  CModalHeader,
  CModalTitle,
} from "@coreui/react";
import { UseModal } from "../../../components/hook/UseModal";
import { ContentShop } from "./Content";
import { UseForm } from "../../../components/hook/UseForm";
import { UseValidShop } from "./Validate";
import { addShopData } from "../../../services/stateShop";
import { useState } from "react";
import { RedCAlert } from "../../../components/redflag/RedCAlert";

export const ShopModal = ({ title }) => {
  const { visible, openModal, closeModal } = UseModal();
  const { formData, setForm, onChange } = UseForm();
  const { validate, validateForm, setValidate } = UseValidShop();
  const [respoErr, setRespoErr] = useState("");

  async function onAdd() {
    if (!validateForm(formData)) {
      return;
    }

    const response = await addShopData(formData);
    if (response.data === "err") {
      setRespoErr(response.message);
      return;
    }
    onClose();
  }

  function onClose() {
    setValidate({});
    setForm({});
    closeModal();
  }

  return (
    <>
      <CButton
        color="secondary"
        className="mb-3"
        onClick={openModal}
        style={{ width: "150px" }}
      >
        {title}
      </CButton>
      <CModal size="lg" visible={visible} onClose={onClose}>
        <CModalHeader>
          <CModalTitle id="header_shop_modal">Shop Data</CModalTitle>
        </CModalHeader>
        <CModalBody>
          <ContentShop
            formData={formData}
            onChange={onChange}
            validate={validate}
          />
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
    </>
  );
};
