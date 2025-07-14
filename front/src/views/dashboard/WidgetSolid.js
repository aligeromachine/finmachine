import { CCard, CCardBody, CCol, CRow, CWidgetStatsB } from "@coreui/react";

export const WidgetSolid = ({ data }) => {
  return (
    <CCard className="mb-4">
      <CCardBody>
        <CRow xs={{ gutter: 4 }}>
          <CCol xs={12} sm={6} xl={4} xxl={3}>
            <CWidgetStatsB
              color="success"
              inverse
              value={data?.year}
              title="Траты за год"
              progress={{ value: 89.9 }}
              text="Lorem ipsum dolor sit amet enim."
            />
          </CCol>
          <CCol xs={12} sm={6} xl={4} xxl={3}>
            <CWidgetStatsB
              color="info"
              inverse
              value={data?.month}
              title="Траты за месяц"
              progress={{ value: 89.9 }}
              text="Lorem ipsum dolor sit amet enim."
            />
          </CCol>
          <CCol xs={12} sm={6} xl={4} xxl={3}>
            <CWidgetStatsB
              color="warning"
              inverse
              value={data?.week}
              title="Траты за неделю"
              progress={{ value: 89.9 }}
              text="Lorem ipsum dolor sit amet enim."
            />
          </CCol>
          <CCol xs={12} sm={6} xl={4} xxl={3}>
            <CWidgetStatsB
              color="primary"
              inverse
              value={data?.day}
              title="Траты за день"
              progress={{ value: 89.9 }}
              text="Lorem ipsum dolor sit amet enim."
            />
          </CCol>
        </CRow>
      </CCardBody>
    </CCard>
  );
};
