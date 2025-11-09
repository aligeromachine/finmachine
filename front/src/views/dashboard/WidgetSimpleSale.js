import { CCard, CCardBody, CCol, CRow, CWidgetStatsE } from "@coreui/react";
import { getStyle } from "@coreui/utils";
import { CChartBar, CChartLine } from "@coreui/react-chartjs";
import CIcon from "@coreui/icons-react";
import {
  cilPeople,
  cilUserFollow,
  cilBasket,
  cilChartPie,
  cilSpeedometer,
  cilSpeech,
} from "@coreui/icons";

export const WidgetSimpleSale = ({ data }) => {
  const random = (min, max) =>
    Math.floor(Math.random() * (max - min + 1) + min);
  return (
    <CCard className="mb-4">
      <CCardBody>
        <CRow xs={{ gutter: 4 }}>
          <CCol xs={12} sm={6} xl={4} xxl={3}>
            <CWidgetStatsE
              chart={
                <CChartLine
                  className="mx-auto"
                  style={{ height: "40px", width: "250px" }}
                  data={{
                    labels: [
                      "M",
                      "T",
                      "W",
                      "T",
                      "F",
                      "S",
                      "S",
                      "M",
                      "T",
                      "W",
                      "T",
                      "F",
                      "S",
                      "S",
                      "M",
                    ],
                    datasets: [
                      {
                        backgroundColor: "transparent",
                        borderColor: getStyle("--cui-info"),
                        borderWidth: 2,
                        data: [
                          random(40, 100),
                          random(40, 100),
                          random(40, 100),
                          random(40, 100),
                          random(40, 100),
                          random(40, 100),
                          random(40, 100),
                          random(40, 100),
                          random(40, 100),
                          random(40, 100),
                          random(40, 100),
                          random(40, 100),
                          random(40, 100),
                          random(40, 100),
                          random(40, 100),
                        ],
                      },
                    ],
                  }}
                  options={{
                    maintainAspectRatio: false,
                    elements: {
                      line: {
                        tension: 0.4,
                      },
                      point: {
                        radius: 0,
                      },
                    },
                    plugins: {
                      legend: {
                        display: false,
                      },
                    },
                    scales: {
                      x: {
                        display: false,
                      },
                      y: {
                        display: false,
                      },
                    },
                  }}
                />
              }
              title="title"
              value="1,123"
            />
          </CCol>
          <CCol xs={12} sm={6} xl={4} xxl={3}>
            <CWidgetStatsE
              chart={
                <CChartLine
                  className="mx-auto"
                  style={{ height: "40px", width: "250px" }}
                  data={{
                    labels: [
                      "M",
                      "T",
                      "W",
                      "T",
                      "F",
                      "S",
                      "S",
                      "M",
                      "T",
                      "W",
                      "T",
                      "F",
                      "S",
                      "S",
                      "M",
                    ],
                    datasets: [
                      {
                        backgroundColor: "transparent",
                        borderColor: getStyle("--cui-danger"),
                        borderWidth: 2,
                        data: [
                          random(40, 100),
                          random(40, 100),
                          random(40, 100),
                          random(40, 100),
                          random(40, 100),
                          random(40, 100),
                          random(40, 100),
                          random(40, 100),
                          random(40, 100),
                          random(40, 100),
                          random(40, 100),
                          random(40, 100),
                          random(40, 100),
                          random(40, 100),
                          random(40, 100),
                        ],
                      },
                    ],
                  }}
                  options={{
                    maintainAspectRatio: false,
                    elements: {
                      line: {
                        tension: 0.4,
                      },
                      point: {
                        radius: 0,
                      },
                    },
                    plugins: {
                      legend: {
                        display: false,
                      },
                    },
                    scales: {
                      x: {
                        display: false,
                      },
                      y: {
                        display: false,
                      },
                    },
                  }}
                />
              }
              title="title"
              value="1,123"
            />
          </CCol>
          <CCol xs={12} sm={6} xl={4} xxl={3}>
            <CWidgetStatsE
              chart={
                <CChartLine
                  className="mx-auto"
                  style={{ height: "40px", width: "250px" }}
                  data={{
                    labels: [
                      "M",
                      "T",
                      "W",
                      "T",
                      "F",
                      "S",
                      "S",
                      "M",
                      "T",
                      "W",
                      "T",
                      "F",
                      "S",
                      "S",
                      "M",
                    ],
                    datasets: [
                      {
                        backgroundColor: "transparent",
                        borderColor: getStyle("--cui-success"),
                        borderWidth: 2,
                        data: [
                          random(40, 100),
                          random(40, 100),
                          random(40, 100),
                          random(40, 100),
                          random(40, 100),
                          random(40, 100),
                          random(40, 100),
                          random(40, 100),
                          random(40, 100),
                          random(40, 100),
                          random(40, 100),
                          random(40, 100),
                          random(40, 100),
                          random(40, 100),
                          random(40, 100),
                        ],
                      },
                    ],
                  }}
                  options={{
                    maintainAspectRatio: false,
                    elements: {
                      line: {
                        tension: 0.4,
                      },
                      point: {
                        radius: 0,
                      },
                    },
                    plugins: {
                      legend: {
                        display: false,
                      },
                    },
                    scales: {
                      x: {
                        display: false,
                      },
                      y: {
                        display: false,
                      },
                    },
                  }}
                />
              }
              title="title"
              value="1,123"
            />
          </CCol>
          <CCol xs={12} sm={6} xl={4} xxl={3}>
            <CWidgetStatsE
              chart={
                <CChartLine
                  className="mx-auto"
                  style={{ height: "40px", width: "250px" }}
                  data={{
                    labels: [
                      "M",
                      "T",
                      "W",
                      "T",
                      "F",
                      "S",
                      "S",
                      "M",
                      "T",
                      "W",
                      "T",
                      "F",
                      "S",
                      "S",
                      "M",
                    ],
                    datasets: [
                      {
                        backgroundColor: "transparent",
                        borderColor: getStyle("--cui-warning"),
                        borderWidth: 2,
                        data: [
                          random(40, 100),
                          random(40, 100),
                          random(40, 100),
                          random(40, 100),
                          random(40, 100),
                          random(40, 100),
                          random(40, 100),
                          random(40, 100),
                          random(40, 100),
                          random(40, 100),
                          random(40, 100),
                          random(40, 100),
                          random(40, 100),
                          random(40, 100),
                          random(40, 100),
                        ],
                      },
                    ],
                  }}
                  options={{
                    maintainAspectRatio: false,
                    elements: {
                      line: {
                        tension: 0.4,
                      },
                      point: {
                        radius: 0,
                      },
                    },
                    plugins: {
                      legend: {
                        display: false,
                      },
                    },
                    scales: {
                      x: {
                        display: false,
                      },
                      y: {
                        display: false,
                      },
                    },
                  }}
                />
              }
              title="title"
              value="1,123"
            />
          </CCol>
        </CRow>
      </CCardBody>
    </CCard>
  );
};
