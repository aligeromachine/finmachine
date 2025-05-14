import React from "react";
import { useModal } from "../../../../components/hook/ModalContext";
import { addCatRow } from "../../../../services/catalog/request";
import { setRowState } from "../../../../services/row/state";
import { SourceContent } from "./Content";
import { UseValid } from "./Validate";

export const CatModal = () => {
  const { isModalOpen, closeModal, formData, onChange, onSet } = useModal();
  const { validate, validateForm, repErr, setRepErr } = UseValid();

  async function onAdd() {
    if (!validateForm(formData)) {
      return;
    }

    onSet(setRowState);
    const response = await addCatRow();
    if (response.data === "err") {
      setRepErr(response.message);
      return;
    }
    closeModal();
  }

  return (
    <SourceContent
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
