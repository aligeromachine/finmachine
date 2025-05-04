import React from "react";
import { ShopContent } from "./ShopContent";
import { UseForm } from "../../../components/hook/UseForm";
import { UseValidShop } from "./Validate";
import { addShopData } from "../../../services/stateShop";
import { useState } from "react";
import { useModal } from "../../../components/hook/ModalContext";

export const ShopModal = () => {
  const { isModalOpen, closeModal } = useModal();
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
    <ShopContent
      visible={isModalOpen}
      onClose={onClose}
      formData={formData}
      onChange={onChange}
      validate={validate}
      respoErr={respoErr}
      onAdd={onAdd}
    />
  );
};
