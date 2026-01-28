import React from 'react';
import { CCardHeader } from '@coreui/react';

export const Header = ({ title }) => {
    return (
        <CCardHeader>
            <strong>{title}</strong>
        </CCardHeader>
    );
};
