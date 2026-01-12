import {
  CAvatar,
  CButton,
  CButtonGroup,
  CCard,
  CCardBody,
  CCardFooter,
  CCardHeader,
  CCol,
  CProgress,
  CRow,
  CTable,
  CTableBody,
  CTableDataCell,
  CTableHead,
  CTableHeaderCell,
  CTableRow,
} from "@coreui/react";
import CIcon from "@coreui/icons-react";
import {
  cibCcAmex,
  cibCcApplePay,
  cibCcMastercard,
  cibCcPaypal,
  cibCcStripe,
  cibCcVisa,
  cibGoogle,
  cibFacebook,
  cibLinkedin,
  cifBr,
  cifEs,
  cifFr,
  cilHouse,
  cifPl,
  cifUs,
  cibTwitter,
  cilDollar,
  cilCalendar,
  cilUser,
  cilEuro,
} from "@coreui/icons";

export const WdBuy = ({ data, daily, shop }) => {
  return (
    <CRow>
      <CCol xs>
        <CCard className="mb-4">
          <CCardHeader>{"Траты"}</CCardHeader>
          <CCardBody>
            <CCol xs={12}>
              <CRow>
                <CCol xs={3}>
                  <div className="border-start border-start-4 border-start-info py-1 px-3">
                    <div className="text-body-primary text-truncate small">
                      Год
                    </div>
                    <div className="fs-5 fw-semibold">{data?.year}</div>
                  </div>
                </CCol>
                <CCol xs={3}>
                  <div className="border-start border-start-4 border-start-danger py-1 px-3 mb-3">
                    <div className="text-body-secondary text-truncate small">
                      Месяц
                    </div>
                    <div className="fs-5 fw-semibold">{data?.month}</div>
                  </div>
                </CCol>
                <CCol xs={3}>
                  <div className="border-start border-start-4 border-start-warning py-1 px-3 mb-3">
                    <div className="text-body-secondary text-truncate small">
                      Неделю
                    </div>
                    <div className="fs-5 fw-semibold">{data?.week}</div>
                  </div>
                </CCol>
                <CCol xs={3}>
                  <div className="border-start border-start-4 border-start-success py-1 px-3 mb-3">
                    <div className="text-body-secondary text-truncate small">
                      День
                    </div>
                    <div className="fs-5 fw-semibold">{data?.day}</div>
                  </div>
                </CCol>
              </CRow>
              <hr className="mt-0" />
            </CCol>
            <CRow>
              <CCol xs={6}>
                {daily?.map((item, index) => (
                  <div className="progress-group mb-4" key={index}>
                    <div className="progress-group-header">
                      <CIcon className="me-2" icon={cilCalendar} size="lg" />
                      <span>{item.title}</span>
                      <span className="ms-auto">{item.amount}</span>
                    </div>
                    <div className="progress-group-bars">
                      <CProgress thin color="info" value={25} />
                    </div>
                  </div>
                ))}
              </CCol>
              <CCol xs={6}>
                {shop?.map((item, index) => (
                  <div className="progress-group mb-4" key={index}>
                    <div className="progress-group-header">
                      <CIcon className="me-2" icon={cilDollar} size="lg" />
                      <span>{item.title}</span>
                      <span className="ms-auto">{item.amount}</span>
                    </div>
                    <div className="progress-group-bars">
                      <CProgress thin color="success" value={25} />
                    </div>
                  </div>
                ))}
              </CCol>
            </CRow>
          </CCardBody>
        </CCard>
      </CCol>
    </CRow>
  );
};
