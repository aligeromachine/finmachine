import { CCard, CCardBody, CCol, CRow, CWidgetStatsB } from "@coreui/react";

export const WidgetSolid = ({ data }) => {
  return (
    <CCard className="mb-4">
      <CCardBody>
        <CRow xs={{ gutter: 4 }}>
          <CCol xs={12} sm={6} xl={4} xxl={3}>
            <CWidgetStatsB
              value={data?.year}
              title="Траты за год"
              progress={{ color: "danger", value: 100 }}
            />
          </CCol>
          <CCol xs={12} sm={6} xl={4} xxl={3}>
            <CWidgetStatsB
              value={data?.month}
              title="Траты за месяц"
              progress={{ color: "primary", value: 100 }}
            />
          </CCol>
          <CCol xs={12} sm={6} xl={4} xxl={3}>
            <CWidgetStatsB
              value={data?.week}
              title="Траты за неделю"
              progress={{ color: "info", value: 100 }}
            />
          </CCol>
          <CCol xs={12} sm={6} xl={4} xxl={3}>
            <CWidgetStatsB
              value={data?.day}
              title="Траты за день"
              progress={{ color: "success", value: 100 }}
            />
          </CCol>
        </CRow>
      </CCardBody>
    </CCard>
  );
};
