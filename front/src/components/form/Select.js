import React from "react";
import { useState, useEffect } from "react";
import { CFormSelect } from "@coreui/react";

export const AsyncFormSelect = ({ onChange, value, name, request }) => {
  const [options, setOptions] = useState([]);
  useEffect(() => {
    const fetchOptions = async () => {
      const data = await request();

      const listOptions = data.map((item) => ({
        value: item.pk,
        label: item.title,
      }));

      const newItems = [{ value: "", label: "-- Choise --", disabled: true }];

      setOptions([...newItems, ...listOptions]);
    };

    fetchOptions();
  }, []);

  return (
    <CFormSelect
      label="Source"
      aria-label="Default select example"
      placeholder="Выберите вариант..."
      value={value}
      name={name}
      onChange={onChange}
      options={options}
    />
  );
};
