import { useState, useCallback } from "react";

export const UseModal = () => {
  const [visible, setVisible] = useState(false);

  const refreshModal = useCallback(() => {
    setVisible(!visible);
  }, []);

  const closeModal = useCallback(() => {
    setVisible(false);
  }, []);

  return {
    visible,
    refreshModal,
    closeModal,
  };
};
