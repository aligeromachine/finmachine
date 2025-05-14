import React from "react";
import { useModal } from "../../../../components/hook/ModalContext";
import { setRowState } from "../../../../services/row/state";
import { addProdRow } from "../../../../services/products/request";
import { ProfitContent } from "./Content";
import { UseValid } from "./Validate";

export const ProdModal = () => {
  const { isModalOpen, closeModal, formData, onChange, onSet } = useModal();
  const { validate, validateForm, repErr, setRepErr } = UseValid();

  async function onAdd() {
    if (!validateForm(formData)) {
      return;
    }

    onSet(setRowState);
    const response = await addProdRow();
    if (response.data === "err") {
      setRepErr(response.message);
      return;
    }
    closeModal();
  }

  return (
    <ProfitContent
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
