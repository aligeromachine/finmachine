import { useState } from "react";
import { useDispatch } from "react-redux";

export const UseForm = () => {
  const [formData, setForm] = useState({});
  const dispatch = useDispatch();

  const onChange = (e) => {
    e.preventDefault();

    setForm({ ...formData, [e.target.name]: e.target.value });
  };

  const onSet = (e, func) => {
    e.preventDefault();

    dispatch(func(formData));
    setForm({});
  };

  return { formData, setForm, onChange, onSet };
};
