import { useState, useCallback } from 'react';
import { isEmpty } from '../../utils/func';

export const UseValidRegister = () => {
    const [validate, setValidate] = useState({});

    const validateForm = useCallback(formData => {
        const newErrors = {};

        if (!formData.username) {
            newErrors.username = 'Имя обязательно';
        }

        if (!formData.email) {
            newErrors.email = 'Email обязателен';
        } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(formData.email)) {
            newErrors.email = 'Некорректный email';
        }

        if (!formData.password) {
            newErrors.password = 'Пароль обязателен';
        } else if (formData.password.length < 6) {
            newErrors.password = 'Пароль должен быть не менее 6 символов';
        }

        if (formData.password !== formData.confirmPassword) {
            newErrors.confirmPassword = 'Пароли не совпадают';
        }

        setValidate(newErrors);
        return isEmpty(newErrors);
    }, []);

    return {
        validate,
        validateForm,
    };
};
