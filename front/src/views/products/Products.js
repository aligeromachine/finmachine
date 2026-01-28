import React from 'react';
import { CCard, CCardBody, CCardHeader, CCol, CRow, CTab, CTabContent, CTabList, CTabPanel, CTabs } from '@coreui/react';
import { ModalProvider } from '../../components/hook/ModalContext';
import { Header } from '../../components/elems/Header';
import { Button } from '../../components/elems/Button';
import { TableProd } from './TableProd';
import { TableCat } from './TableCat';
import { CatModal } from './modal/cat/Base';
import { ProdModal } from './modal/prod/Base';
import { Auth } from '../../components/auth/Auth';

export const DataProducts = () => {
    return (
        <Auth>
            <CRow>
                <CCol xs={12}>
                    <CCard className="mb-4">
                        <Header title={'DataProducts'} />
                        <CCardBody>
                            <CTabs defaultActiveItemKey="product">
                                <CTabList variant="tabs">
                                    <CTab itemKey="product">Product</CTab>
                                    <CTab itemKey="catalog">Catalog</CTab>
                                </CTabList>
                                <CTabContent>
                                    <CTabPanel className="p-3" itemKey="product">
                                        <ModalProvider>
                                            <ProdModal />
                                            <Button title={'Add Products'} />
                                            <TableProd />
                                        </ModalProvider>
                                    </CTabPanel>
                                    <CTabPanel className="p-3" itemKey="catalog">
                                        <ModalProvider>
                                            <CatModal />
                                            <Button title={'Add Catalog'} />
                                            <TableCat />
                                        </ModalProvider>
                                    </CTabPanel>
                                </CTabContent>
                            </CTabs>
                        </CCardBody>
                    </CCard>
                </CCol>
            </CRow>
        </Auth>
    );
};
