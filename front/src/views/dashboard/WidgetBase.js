import { CCard, CCardBody, CCol, CRow, CWidgetStatsF } from "@coreui/react";
import CIcon from "@coreui/icons-react";
import { cilUser, cilSettings, cilMoon, cilBell } from "@coreui/icons";

export const WidgetBase = () => {
  return (
    <CCard className="mb-4">
      <CCardBody>
        <CRow xs={{ gutter: 4 }}>
          <CCol xs={12} sm={6} xl={4} xxl={3}>
            <CWidgetStatsF
              icon={<CIcon width={24} icon={cilSettings} size="xl" />}
              title="income"
              value="$1.999,50"
              color="primary"
            />
          </CCol>
          <CCol xs={12} sm={6} xl={4} xxl={3}>
            <CWidgetStatsF
              icon={<CIcon width={24} icon={cilUser} size="xl" />}
              title="income"
              value="$1.999,50"
              color="info"
            />
          </CCol>
          <CCol xs={12} sm={6} xl={4} xxl={3}>
            <CWidgetStatsF
              icon={<CIcon width={24} icon={cilMoon} size="xl" />}
              title="income"
              value="$1.999,50"
              color="warning"
            />
          </CCol>
          <CCol xs={12} sm={6} xl={4} xxl={3}>
            <CWidgetStatsF
              icon={<CIcon width={24} icon={cilBell} size="xl" />}
              title="income"
              value="$1.999,50"
              color="danger"
            />
          </CCol>
        </CRow>
      </CCardBody>
    </CCard>
  );
};
