import { CCard, CCardBody, CCol, CRow } from '@coreui/react';
import { ModalProvider } from '../../components/hook/ModalContext';
import { Header } from '../../components/elems/Header';
import { Button } from '../../components/elems/Button';
import { TableBuy } from './Table';
import { BuysModal } from './modal/Base';
import { Auth } from '../../components/auth/Auth';

export const DataTransactions = () => {
    return (
        <Auth>
            <ModalProvider>
                <CRow>
                    <CCol xs={12}>
                        <CCard className="mb-4">
                            <Header title={'DataTransactions'} />
                            <CCardBody>
                                <BuysModal />
                                <Button title={'Add Buy'} />
                                <TableBuy />
                            </CCardBody>
                        </CCard>
                    </CCol>
                </CRow>
            </ModalProvider>
        </Auth>
    );
};
