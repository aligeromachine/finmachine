import { CCard, CCardBody, CCol, CRow, CWidgetStatsB } from "@coreui/react";

export const WidgetSolid = () => {
  return (
    <CCard className="mb-4">
      <CCardBody>
        <CRow xs={{ gutter: 4 }}>
          <CCol xs={12} sm={6} xl={4} xxl={3}>
            <CWidgetStatsB
              color="success"
              inverse
              value="89.9%"
              title="Widget title"
              progress={{ value: 89.9 }}
              text="Lorem ipsum dolor sit amet enim."
            />
          </CCol>
          <CCol xs={12} sm={6} xl={4} xxl={3}>
            <CWidgetStatsB
              color="info"
              inverse
              value="12.124"
              title="Widget title"
              progress={{ value: 89.9 }}
              text="Lorem ipsum dolor sit amet enim."
            />
          </CCol>
          <CCol xs={12} sm={6} xl={4} xxl={3}>
            <CWidgetStatsB
              color="warning"
              inverse
              value="$98.111,00"
              title="Widget title"
              progress={{ value: 89.9 }}
              text="Lorem ipsum dolor sit amet enim."
            />
          </CCol>
          <CCol xs={12} sm={6} xl={4} xxl={3}>
            <CWidgetStatsB
              color="primary"
              inverse
              value="2 TB"
              title="Widget title"
              progress={{ value: 89.9 }}
              text="Lorem ipsum dolor sit amet enim."
            />
          </CCol>
        </CRow>
      </CCardBody>
    </CCard>
  );
};
