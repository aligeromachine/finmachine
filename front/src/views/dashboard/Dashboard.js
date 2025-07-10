import React from "react";
import classNames from "classnames";
import { Auth } from "../../components/auth/Auth";

import {
  CAvatar,
  CButton,
  CButtonGroup,
  CCard,
  CCardBody,
  CCardFooter,
  CCardHeader,
  CCol,
  CProgress,
  CRow,
  CTable,
  CTableBody,
  CTableDataCell,
  CTableHead,
  CTableHeaderCell,
  CTableRow,
  CWidgetStatsB,
  CWidgetStatsC,
  CWidgetStatsE,
  CWidgetStatsF,
} from "@coreui/react";
import CIcon from "@coreui/icons-react";
import {
  cibCcAmex,
  cibCcApplePay,
  cibCcMastercard,
  cibCcPaypal,
  cibCcStripe,
  cibCcVisa,
  cibGoogle,
  cibFacebook,
  cibLinkedin,
  cifBr,
  cifEs,
  cifFr,
  cifIn,
  cifPl,
  cifUs,
  cibTwitter,
  cilCloudDownload,
  cilPeople,
  cilUser,
  cilUserFemale,
  cilSettings,
  cilMoon,
  cilBell,
  cilUserFollow,
  cilBasket,
  cilChartPie,
  cilSpeedometer,
  cilSpeech,
} from "@coreui/icons";

import WidgetsDropdown from "./Widgets1";
import { MainChart } from "./MainChart";

export const Dashboard = () => {
  const progressExample = [
    { title: "Visits", value: "29.703 Users", percent: 40, color: "success" },
    { title: "Unique", value: "24.093 Users", percent: 20, color: "info" },
    {
      title: "Pageviews",
      value: "78.706 Views",
      percent: 60,
      color: "warning",
    },
    { title: "New Users", value: "22.123 Users", percent: 80, color: "danger" },
    {
      title: "Bounce Rate",
      value: "Average Rate",
      percent: 40.15,
      color: "primary",
    },
  ];

  return (
    <Auth>
      <WidgetsDropdown className="mb-4" />
      <CCard className="mb-4">
        <CCardBody>
          <CRow>
            <CCol sm={5}>
              <h4 id="traffic" className="card-title mb-0">
                Traffic
              </h4>
              <div className="small text-body-secondary">
                January - July 2023
              </div>
            </CCol>
            <CCol sm={7} className="d-none d-md-block">
              <CButton color="primary" className="float-end">
                <CIcon icon={cilCloudDownload} />
              </CButton>
              <CButtonGroup className="float-end me-3">
                {["Day", "Month", "Year"].map((value) => (
                  <CButton
                    color="outline-secondary"
                    key={value}
                    className="mx-0"
                    active={value === "Month"}
                  >
                    {value}
                  </CButton>
                ))}
              </CButtonGroup>
            </CCol>
          </CRow>
          <MainChart />
        </CCardBody>
        <CCardFooter>
          <CRow
            xs={{ cols: 1, gutter: 4 }}
            sm={{ cols: 2 }}
            lg={{ cols: 4 }}
            xl={{ cols: 5 }}
            className="mb-2 text-center"
          >
            {progressExample.map((item, index, items) => (
              <CCol
                className={classNames({
                  "d-none d-xl-block": index + 1 === items.length,
                })}
                key={index}
              >
                <div className="text-body-secondary">{item.title}</div>
                <div className="fw-semibold text-truncate">
                  {item.value} ({item.percent}%)
                </div>
                <CProgress
                  thin
                  className="mt-2"
                  color={item.color}
                  value={item.percent}
                />
              </CCol>
            ))}
          </CRow>
        </CCardFooter>
      </CCard>
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

      <CCard className="mb-4">
        <CCardBody>
          <CRow xs={{ gutter: 4 }}>
            <CCol xs={6} lg={4} xxl={2}>
              <CWidgetStatsC
                icon={<CIcon icon={cilPeople} height={36} />}
                value="87.500"
                title="Visitors"
                progress={{ color: "info", value: 75 }}
              />
            </CCol>
            <CCol xs={6} lg={4} xxl={2}>
              <CWidgetStatsC
                icon={<CIcon icon={cilUserFollow} height={36} />}
                value="385"
                title="New Clients"
                progress={{ color: "success", value: 75 }}
              />
            </CCol>
            <CCol xs={6} lg={4} xxl={2}>
              <CWidgetStatsC
                icon={<CIcon icon={cilBasket} height={36} />}
                value="1238"
                title="Products sold"
                progress={{ color: "warning", value: 75 }}
              />
            </CCol>
            <CCol xs={6} lg={4} xxl={2}>
              <CWidgetStatsC
                icon={<CIcon icon={cilChartPie} height={36} />}
                value="28%"
                title="Returning Visitors"
                progress={{ color: "primary", value: 75 }}
              />
            </CCol>
            <CCol xs={6} lg={4} xxl={2}>
              <CWidgetStatsC
                icon={<CIcon icon={cilSpeedometer} height={36} />}
                value="5:34:11"
                title="Avg. Time"
                progress={{ color: "danger", value: 75 }}
              />
            </CCol>
            <CCol xs={6} lg={4} xxl={2}>
              <CWidgetStatsC
                icon={<CIcon icon={cilSpeech} height={36} />}
                value="972"
                title="Comments"
                progress={{ color: "info", value: 75 }}
              />
            </CCol>
          </CRow>
        </CCardBody>
      </CCard>
    </Auth>
  );
};
