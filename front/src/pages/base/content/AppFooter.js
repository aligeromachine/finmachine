import React from 'react';
import { CFooter } from '@coreui/react';

export const AppFooter = React.memo(() => {
    return (
        <CFooter className="px-4">
            <div>
                <span className="ms-1">&copy; 2026 Money.</span>
            </div>
            <div className="ms-auto">
                <span className="me-1">Powered by AligeroMachine</span>
            </div>
        </CFooter>
    );
});
