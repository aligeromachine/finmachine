import { CCard, CCardBody, CCardHeader, CCol, CRow } from '@coreui/react';

export const WdBase = ({ data }) => {
    return (
        <CRow>
            <CCol xs>
                <CCard className="mb-4">
                    <CCardHeader>{'Траты'}</CCardHeader>
                    <CCardBody>
                        <CRow>
                            <CCol xs={12}>
                                <CRow>
                                    <CCol xs={3}>
                                        <div className="border-start border-start-4 border-start-info py-1 px-3">
                                            <div className="text-body-primary text-truncate small">New Clients</div>
                                            <div className="fs-5 fw-semibold">9,123</div>
                                        </div>
                                    </CCol>
                                    <CCol xs={3}>
                                        <div className="border-start border-start-4 border-start-danger py-1 px-3 mb-3">
                                            <div className="text-body-secondary text-truncate small">Recurring Clients</div>
                                            <div className="fs-5 fw-semibold">22,643</div>
                                        </div>
                                    </CCol>
                                    <CCol xs={3}>
                                        <div className="border-start border-start-4 border-start-warning py-1 px-3 mb-3">
                                            <div className="text-body-secondary text-truncate small">Pageviews</div>
                                            <div className="fs-5 fw-semibold">78,623</div>
                                        </div>
                                    </CCol>
                                    <CCol xs={3}>
                                        <div className="border-start border-start-4 border-start-success py-1 px-3 mb-3">
                                            <div className="text-body-secondary text-truncate small">Organic</div>
                                            <div className="fs-5 fw-semibold">49,123</div>
                                        </div>
                                    </CCol>
                                </CRow>
                                <hr className="mt-0" />
                            </CCol>
                        </CRow>
                    </CCardBody>
                </CCard>
            </CCol>
        </CRow>
    );
};
