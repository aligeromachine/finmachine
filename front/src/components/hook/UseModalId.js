import { useState, useCallback } from 'react';

export const UseModalId = () => {
    const [form, setForm] = useState({
        visible: false,
        id: 0,
    });

    const openModal = useCallback(id => {
        setForm({ visible: !form.visible, id: id });
    }, []);

    const closeModal = useCallback(() => {
        setForm({ visible: false, id: 0 });
    }, []);

    return {
        form,
        openModal,
        closeModal,
    };
};
