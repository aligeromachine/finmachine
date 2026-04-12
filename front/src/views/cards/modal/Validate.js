import { useState, useCallback } from 'react';
import { isEmpty } from '../../../utils/func';

export const UseValid = () => {
    const [validate, setValidate] = useState({});
    const [repErr, setRepErr] = useState('');

    const validateForm = useCallback(formData => {
        const newErrors = {};

        if (!formData.title) {
            newErrors.title = 'Title обязательно';
        }

        if (!formData.amount) {
            newErrors.amount = 'Amount обязателен';
        } else if (!/^\d*\.?\d*$/.test(formData.amount)) {
            newErrors.amount = 'Некорректный amount';
        }

        if (!formData.number) {
            newErrors.number = 'Number обязательно';
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
