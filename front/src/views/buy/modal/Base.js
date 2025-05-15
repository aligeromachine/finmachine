import React from "react";
import { useModal } from "../../../components/hook/ModalContext";
import { setRowState } from "../../../services/row/state";
import { addBuyRow } from "../../../services/buys/request";
import { ProfitContent } from "./Content";
import { UseValid } from "./Validate";

export const BuysModal = () => {
  const { isModalOpen, closeModal, formData, onChange, onSet, isEdit } =
    useModal();
  const { validate, validateForm, repErr, setRepErr } = UseValid();

  async function onAdd() {
    if (!validateForm(formData)) {
      return;
    }

    onSet(setRowState);
    const response = await addBuyRow();
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
      isEdit={isEdit}
    />
  );
};
