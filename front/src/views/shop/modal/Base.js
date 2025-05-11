import React from "react";
import { ShopContent } from "./Content";
import { UseValid } from "./Validate";
import { addShopRow } from "../../../services/stateShop";
import { useModal } from "../../../components/hook/ModalContext";
import { setRowState } from "../../../services/stateRow";

export const ShopModal = () => {
  const { isModalOpen, closeModal, formData, onChange, onSet } = useModal();
  const { validate, validateForm, repErr, setRepErr } = UseValid();

  async function onAdd() {
    if (!validateForm(formData)) {
      return;
    }

    onSet(setRowState);
    const response = await addShopRow();
    if (response.data === "err") {
      setRepErr(response.message);
      return;
    }
    closeModal();
  }

  return (
    <ShopContent
      visible={isModalOpen}
      onClose={closeModal}
      formData={formData}
      onChange={onChange}
      validate={validate}
      repErr={repErr}
      onAdd={onAdd}
    />
  );
};
