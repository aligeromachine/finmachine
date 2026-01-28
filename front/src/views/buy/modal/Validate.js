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

        if (!formData.shop) {
            newErrors.shop = 'Shop обязательно';
        }

        if (!formData.cat) {
            newErrors.cat = 'Catalog обязательно';
        }

        if (!formData.prod) {
            newErrors.prod = 'Products обязательно';
        }

        if (!formData.amount) {
            newErrors.amount = 'Amount обязательно';
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
