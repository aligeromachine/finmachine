import React from "react";
import { CardsContent } from "./CardsContent";
import { UseValid } from "./Validate";
import { addCardsRow } from "../../../services/stateCards";
import { useState } from "react";
import { useModal } from "../../../components/hook/ModalContext";
import { setRowState } from "../../../services/stateRow";

export const CardsModal = () => {
  const { isModalOpen, closeModal, formData, onChange, onSet } = useModal();
  const { validate, validateForm } = UseValid();
  const [respoErr, setRespoErr] = useState("");

  async function onAdd() {
    if (!validateForm(formData)) {
      return;
    }

    onSet(setRowState);
    const response = await addCardsRow();
    if (response.data === "err") {
      setRespoErr(response.message);
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
      respoErr={respoErr}
      onAdd={onAdd}
    />
  );
};
