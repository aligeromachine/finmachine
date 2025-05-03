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
import { addShopThunk } from "../../../services/stateShop";
import { useState } from "react";
import { RedCAlert } from "../../../components/redflag/RedCAlert";

export const ShopModal = ({ title }) => {
  const { visible, openModal, closeModal } = UseModal();
  const { formData, onChange } = UseForm();
  const { validate, validateForm } = UseValidShop();
  const [respoErr, setRespoErr] = useState("");

  async function onClick(e) {
    e.preventDefault();

    if (!validateForm(formData)) {
      return;
    }

    const response = await addShopThunk(formData);
    if (response.data === "err") {
      setRespoErr(response.message);
      return;
    }
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
      <CModal size="lg" visible={visible} onClose={closeModal}>
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
          <CButton color="secondary" onClick={closeModal}>
            Close
          </CButton>
          <CButton color="primary" onClick={onClick}>
            Save changes
          </CButton>
        </CModalFooter>
      </CModal>
    </>
  );
};
