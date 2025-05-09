import React, { useEffect } from "react";
import { ShopContent } from "./ShopContent";
import { UseValidShop } from "./Validate";
import { addShopRow } from "../../../services/stateShop";
import { useState } from "react";
import { useModal } from "../../../components/hook/ModalContext";
import { setRowState } from "../../../services/stateRow";

export const ShopModal = () => {
  const { isModalOpen, closeModal, formData, onChange, onSet } = useModal();
  const { validate, validateForm } = UseValidShop();
  const [respoErr, setRespoErr] = useState("");

  async function onAdd() {
    if (!validateForm(formData)) {
      return;
    }

    onSet(setRowState);
    const response = await addShopRow();
    if (response.data === "err") {
      setRespoErr(response.message);
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
      respoErr={respoErr}
      onAdd={onAdd}
    />
  );
};
