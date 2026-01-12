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

export const WdStat = ({ data, card }) => {
  return (
    <CCard className="mb-4">
      <CCardBody>
        <CRow xs={{ gutter: 4 }}>
          <CCol xs={6} lg={4} xxl={2}>
            <CWidgetStatsC
              icon={<CIcon icon={cilCash} height={36} />}
              value={data?.cash}
              title="В кошельке"
              progress={{ color: "info", value: 100 }}
            />
          </CCol>
          <CCol xs={6} lg={4} xxl={2}>
            <CWidgetStatsC
              icon={<CIcon icon={cilBalanceScale} height={36} />}
              value={data?.year}
              title="Прибыль за год"
              progress={{ color: "warning", value: 100 }}
            />
          </CCol>
          <CCol xs={6} lg={4} xxl={2}>
            <CWidgetStatsC
              icon={<CIcon icon={cilBank} height={36} />}
              value={data?.cards}
              title="Сумма на карточках"
              progress={{ color: "success", value: 100 }}
            />
          </CCol>
          <CCol xs={6} lg={4} xxl={2}>
            <CWidgetStatsC
              icon={<CIcon icon={cilChartPie} height={36} />}
              value={card?.one?.amount}
              title={card?.one?.title}
              progress={{ color: "primary", value: 100 }}
            />
          </CCol>
          <CCol xs={6} lg={4} xxl={2}>
            <CWidgetStatsC
              icon={<CIcon icon={cilFire} height={36} />}
              value={card?.two?.amount}
              title={card?.two?.title}
              progress={{ color: "danger", value: 100 }}
            />
          </CCol>
          <CCol xs={6} lg={4} xxl={2}>
            <CWidgetStatsC
              icon={<CIcon icon={cilLibrary} height={36} />}
              value={card?.three?.amount}
              title={card?.three?.title}
              progress={{ color: "info", value: 100 }}
            />
          </CCol>
        </CRow>
      </CCardBody>
    </CCard>
  );
};
