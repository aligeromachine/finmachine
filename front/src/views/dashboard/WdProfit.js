import {
  CCard,
  CCardBody,
  CCol,
  CRow,
  CWidgetStatsB,
  CCardHeader,
} from "@coreui/react";

export const WdProfit = ({ data }) => {
  return (
    <CCard className="mb-4">
      <CCardHeader>{"Доход"}</CCardHeader>
      <CCardBody>
        <CRow xs={{ gutter: 4 }}>
          <CCol xs={12} sm={6} xl={4} xxl={3}>
            <CWidgetStatsB
              value={data?.year}
              title="Год"
              progress={{ color: "danger", value: 100 }}
            />
          </CCol>
          <CCol xs={12} sm={6} xl={4} xxl={3}>
            <CWidgetStatsB
              value={data?.month}
              title="Месяц"
              progress={{ color: "primary", value: 100 }}
            />
          </CCol>
          <CCol xs={12} sm={6} xl={4} xxl={3}>
            <CWidgetStatsB
              value={data?.week}
              title="Неделю"
              progress={{ color: "info", value: 100 }}
            />
          </CCol>
          <CCol xs={12} sm={6} xl={4} xxl={3}>
            <CWidgetStatsB
              value={data?.day}
              title="День"
              progress={{ color: "success", value: 100 }}
            />
          </CCol>
        </CRow>
      </CCardBody>
    </CCard>
  );
};
