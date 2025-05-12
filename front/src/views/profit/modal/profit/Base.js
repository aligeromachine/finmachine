import React from "react";
import { ProfitContent } from "./Content";
import { UseValid } from "./Validate";
import { addProfitRow } from "../../../../services/profit/request";
import { useModal } from "../../../../components/hook/ModalContext";
import { setRowState } from "../../../../services/row/state";

export const ProfitModal = () => {
  const { isModalOpen, closeModal, formData, onChange, onSet } = useModal();
  const { validate, validateForm, repErr, setRepErr } = UseValid();

  async function onAdd() {
    if (!validateForm(formData)) {
      return;
    }

    onSet(setRowState);
    const response = await addProfitRow();
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
