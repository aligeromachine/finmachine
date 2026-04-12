import { useState } from 'react';
import { useDispatch } from 'react-redux';

export const UseForm = () => {
    const [formData, setForm] = useState({});
    const dispatch = useDispatch();

    const onChange = e => {
        e.preventDefault();

        setForm({ ...formData, [e.target.name]: e.target.value });
    };

    const onSet = func => {
        dispatch(func({ ...formData }));
        setForm({});
    };

    const onOpen = data => {
        setForm({ ...formData, ...data });
    };

    return { formData, setForm, onChange, onSet, onOpen };
};
