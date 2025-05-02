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
import { useDispatch } from "react-redux";
import { addShopThunk } from "../../../services/stateShop";
import { ToastLive } from "../../../components/toast/SimpleToast";

export const ShopModal = ({ title }) => {
  const dispatch = useDispatch();

  const { visible, openModal, closeModal } = UseModal();
  const { formData, onChange } = UseForm();
  const { validate, validateForm } = UseValidShop();

  async function onClick(e) {
    e.preventDefault();

    if (!validateForm(formData)) {
      return;
    }

    const response = dispatch(addShopThunk(formData)).unwrap();
    const result = await response;
    if (result.data === "err") {
      alert(result.message);
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
