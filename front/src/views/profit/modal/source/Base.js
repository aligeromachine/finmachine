import React from "react";
import { SourceContent } from "./Content";
import { UseValid } from "./Validate";
import { addSourceRow } from "../../../../services/source/request";
import { useModal } from "../../../../components/hook/ModalContext";
import { setRowState } from "../../../../services/row/state";

export const SourceModal = () => {
  const { isModalOpen, closeModal, formData, onChange, onSet } = useModal();
  const { validate, validateForm, repErr, setRepErr } = UseValid();

  async function onAdd() {
    if (!validateForm(formData)) {
      return;
    }

    onSet(setRowState);
    const response = await addSourceRow();
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
