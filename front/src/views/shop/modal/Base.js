import React from "react";
import { useModal } from "../../../components/hook/ModalContext";
import { setRowState } from "../../../services/row/state";
import { addShopRow } from "../../../services/shop/request";
import { ShopContent } from "./Content";
import { UseValid } from "./Validate";

export const ShopModal = () => {
  const { isModalOpen, closeModal, formData, onChange, onSet, isEdit } = useModal();
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
    if (isEdit) {
      closeModal();
    }
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
