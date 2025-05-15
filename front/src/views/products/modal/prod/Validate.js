import { useState, useCallback } from "react";
import { isEmpty } from "../../../../utils/func";

export const UseValid = () => {
  const [validate, setValidate] = useState({});
  const [repErr, setRepErr] = useState("");

  const validateForm = useCallback((formData) => {
    const newErrors = {};

    if (!formData.title) {
      newErrors.title = "Title обязательно";
    }

    if (!formData.catalog) {
      newErrors.catalog = "Catalog обязательно";
    }

    setValidate(newErrors);
    return isEmpty(newErrors);
  }, []);

  return {
    validate,
    validateForm,
    repErr,
    setRepErr,
  };
};
