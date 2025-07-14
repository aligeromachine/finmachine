import { CCard, CCardBody, CCol, CRow, CWidgetStatsF } from "@coreui/react";
import CIcon from "@coreui/icons-react";
import { cilUser, cilSettings, cilMoon, cilBell } from "@coreui/icons";

export const WidgetBase = ({ data }) => {
  return (
    <CCard className="mb-4">
      <CCardBody>
        <CRow xs={{ gutter: 4 }}>
          <CCol xs={12} sm={6} xl={4} xxl={3}>
            <CWidgetStatsF
              icon={<CIcon width={24} icon={cilMoon} size="xl" />}
              title="Доход за год"
              value={data?.year}
              color="warning"
            />
          </CCol>
          <CCol xs={12} sm={6} xl={4} xxl={3}>
            <CWidgetStatsF
              icon={<CIcon width={24} icon={cilBell} size="xl" />}
              title="Доход за месяц"
              value={data?.month}
              color="danger"
            />
          </CCol>
          <CCol xs={12} sm={6} xl={4} xxl={3}>
            <CWidgetStatsF
              icon={<CIcon width={24} icon={cilSettings} size="xl" />}
              title="Доход за неделю"
              value={data?.week}
              color="primary"
            />
          </CCol>
          <CCol xs={12} sm={6} xl={4} xxl={3}>
            <CWidgetStatsF
              icon={<CIcon width={24} icon={cilUser} size="xl" />}
              title="Доход за день"
              value={data?.day}
              color="info"
            />
          </CCol>
        </CRow>
      </CCardBody>
    </CCard>
  );
};
