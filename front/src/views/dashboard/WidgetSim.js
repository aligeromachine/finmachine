import { CCard, CCardBody, CCol, CRow, CWidgetStatsC } from "@coreui/react";
import CIcon from "@coreui/icons-react";
import {
  cilBalanceScale,
  cilBank,
  cilCash,
  cilChartPie,
  cilFire,
  cilLibrary,
} from "@coreui/icons";

export const WidgetSim = ({ data, card }) => {
  return (
    <CCard className="mb-4">
      <CCardBody>
        <CRow xs={{ gutter: 4 }}>
          <CCol xs={6} lg={4} xxl={2}>
            <CWidgetStatsC
              icon={<CIcon icon={cilBank} height={36} />}
              value={data?.card_sum}
              title="На карточках"
              progress={{ color: "success", value: 75 }}
            />
          </CCol>
          <CCol xs={6} lg={4} xxl={2}>
            <CWidgetStatsC
              icon={<CIcon icon={cilCash} height={36} />}
              value={data?.money_cash}
              title="В кошельке"
              progress={{ color: "info", value: 75 }}
            />
          </CCol>
          <CCol xs={6} lg={4} xxl={2}>
            <CWidgetStatsC
              icon={<CIcon icon={cilBalanceScale} height={36} />}
              value={data?.capital_year}
              title="Прибыль за год"
              progress={{ color: "warning", value: 75 }}
            />
          </CCol>
          <CCol xs={6} lg={4} xxl={2}>
            <CWidgetStatsC
              icon={<CIcon icon={cilChartPie} height={36} />}
              value={card?.one_sum}
              title={card?.one_name}
              progress={{ color: "primary", value: 75 }}
            />
          </CCol>
          <CCol xs={6} lg={4} xxl={2}>
            <CWidgetStatsC
              icon={<CIcon icon={cilFire} height={36} />}
              value={card?.two_sum}
              title={card?.two_name}
              progress={{ color: "danger", value: 75 }}
            />
          </CCol>
          <CCol xs={6} lg={4} xxl={2}>
            <CWidgetStatsC
              icon={<CIcon icon={cilLibrary} height={36} />}
              value={card?.three_sum}
              title={card?.three_name}
              progress={{ color: "info", value: 75 }}
            />
          </CCol>
        </CRow>
      </CCardBody>
    </CCard>
  );
};
