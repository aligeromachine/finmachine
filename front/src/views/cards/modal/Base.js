import React from "react";
import { CardsContent } from "./Content";
import { UseValid } from "./Validate";
import { addCardsRow } from "../../../services/cards/request";
import { setRowState } from "../../../services/row/state";
import { useModal } from "../../../components/hook/ModalContext";

export const CardsModal = () => {
  const { isModalOpen, closeModal, formData, onChange, onSet } = useModal();
  const { validate, validateForm, repErr, setRepErr } = UseValid();

  async function onAdd() {
    if (!validateForm(formData)) {
      return;
    }

    onSet(setRowState);
    const response = await addCardsRow();
    if (response.data === "err") {
      setRepErr(response.message);
      return;
    }
    closeModal();
  }

  return (
    <CardsContent
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
