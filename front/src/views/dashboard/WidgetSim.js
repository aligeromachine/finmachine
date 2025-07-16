import { CCard, CCardBody, CCol, CRow, CWidgetStatsC } from "@coreui/react";
import CIcon from "@coreui/icons-react";
import {
  cilPeople,
  cilUserFollow,
  cilBasket,
  cilChartPie,
  cilSpeedometer,
  cilSpeech,
} from "@coreui/icons";

export const WidgetSim = ({ data, card }) => {
  return (
    <CCard className="mb-4">
      <CCardBody>
        <CRow xs={{ gutter: 4 }}>
          <CCol xs={6} lg={4} xxl={2}>
            <CWidgetStatsC
              icon={<CIcon icon={cilPeople} height={36} />}
              value={data?.money_cash}
              title="В кошельке"
              progress={{ color: "info", value: 75 }}
            />
          </CCol>
          <CCol xs={6} lg={4} xxl={2}>
            <CWidgetStatsC
              icon={<CIcon icon={cilUserFollow} height={36} />}
              value={data?.card_sum}
              title="На карточках"
              progress={{ color: "success", value: 75 }}
            />
          </CCol>
          <CCol xs={6} lg={4} xxl={2}>
            <CWidgetStatsC
              icon={<CIcon icon={cilBasket} height={36} />}
              value={data?.capital_year}
              title="Прибыль"
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
              icon={<CIcon icon={cilSpeedometer} height={36} />}
              value={card?.two_name}
              title={card?.two_sum}
              progress={{ color: "danger", value: 75 }}
            />
          </CCol>
          <CCol xs={6} lg={4} xxl={2}>
            <CWidgetStatsC
              icon={<CIcon icon={cilSpeech} height={36} />}
              value={card?.three_name}
              title={card?.three_sum}
              progress={{ color: "info", value: 75 }}
            />
          </CCol>
        </CRow>
      </CCardBody>
    </CCard>
  );
};
