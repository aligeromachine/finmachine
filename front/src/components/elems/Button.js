import React from 'react';
import { CButton } from '@coreui/react';
import { useModal } from '../hook/ModalContext';

export const Button = ({ title }) => {
    const { openModal } = useModal();

    return (
        <CButton color="secondary" className="mb-3" onClick={() => openModal(false)} style={{ width: '150px' }}>
            {title}
        </CButton>
    );
};

export const ButtonBase = ({ title, onClick }) => {
    return (
        <CButton color="secondary" className="mb-3" onClick={onClick} style={{ width: '150px' }}>
            {title}
        </CButton>
    );
};
