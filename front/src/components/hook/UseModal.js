import { useState, useCallback } from 'react';

export const UseModal = () => {
    const [visible, setVisible] = useState(false);

    const openModal = useCallback(() => {
        setVisible(!visible);
    }, []);

    const closeModal = useCallback(() => {
        setVisible(false);
    }, []);

    return {
        visible,
        openModal,
        closeModal,
    };
};
