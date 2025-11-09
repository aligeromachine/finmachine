import { CCard, CCardBody, CCol, CRow, CWidgetStatsF } from "@coreui/react";
import CIcon from "@coreui/icons-react";
import { cilBold, cilBookmark, cilApple, cilBank } from "@coreui/icons";

export const WidgetBase = ({ data }) => {
  return (
    <CCard className="mb-4">
      <CCardBody>
        <CRow xs={{ gutter: 4 }}>
          <CCol xs={12} sm={6} xl={4} xxl={3}>
            <CWidgetStatsF
              icon={<CIcon width={24} icon={cilBank} size="xl" />}
              title="Доход за год"
              value={data?.year}
              color="danger"
            />
          </CCol>
          <CCol xs={12} sm={6} xl={4} xxl={3}>
            <CWidgetStatsF
              icon={<CIcon width={24} icon={cilApple} size="xl" />}
              title="Доход за месяц"
              value={data?.month}
              color="primary"
            />
          </CCol>
          <CCol xs={12} sm={6} xl={4} xxl={3}>
            <CWidgetStatsF
              icon={<CIcon width={24} icon={cilBookmark} size="xl" />}
              title="Доход за неделю"
              value={data?.week}
              color="info"
            />
          </CCol>
          <CCol xs={12} sm={6} xl={4} xxl={3}>
            <CWidgetStatsF
              icon={<CIcon width={24} icon={cilBold} size="xl" />}
              title="Доход за день"
              value={data?.day}
              color="success"
            />
          </CCol>
        </CRow>
      </CCardBody>
    </CCard>
  );
};
