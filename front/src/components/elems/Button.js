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

export const ButtonBase = props => {
    return (
        <CButton {...props} color="secondary" className="mb-3" onClick={props.onClick}>
            {props.title}
        </CButton>
    );
};

export const ButtonLog = ({ title, onClick }) => {
    return (
        <CButton color="secondary" className="mb-3" onClick={onClick} style={{ width: '150px' }}>
            {title}
        </CButton>
    );
};

export const ButtonDanger = ({ title, onClick }) => {
    return (
        <CButton color="danger" className="mb-3" onClick={onClick} style={{ width: '150px' }}>
            {title}
        </CButton>
    );
};
