import React from "react";
import { useModal } from "../../../components/hook/ModalContext";
import { addCardsRow } from "../../../services/cards/request";
import { setRowState } from "../../../services/row/state";
import { CardsContent } from "./Content";
import { UseValid } from "./Validate";

export const CardsModal = () => {
  // eslint-disable-next-line prettier/prettier
  const { isModalOpen, closeModal, formData, onChange, onSet, isEdit } = useModal();
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
    if (isEdit) {
      closeModal();
    }
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
