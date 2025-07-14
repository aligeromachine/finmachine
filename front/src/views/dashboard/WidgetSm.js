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

export const WidgetSm = ({ data }) => {
  const random = (min, max) =>
    Math.floor(Math.random() * (max - min + 1) + min);
  return (
    <CCard className="mb-4">
      <CCardBody>
        <CRow xs={{ gutter: 4 }}>
          <CCol sm={4} md={3} xl={2}>
            <CWidgetStatsE
              chart={
                <CChartBar
                  className="mx-auto"
                  style={{ height: "40px", width: "80px" }}
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
                        backgroundColor: getStyle("--cui-danger"),
                        borderColor: "transparent",
                        borderWidth: 1,
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
          <CCol sm={4} md={3} xl={2}>
            <CWidgetStatsE
              chart={
                <CChartBar
                  className="mx-auto"
                  style={{ height: "40px", width: "80px" }}
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
                        backgroundColor: getStyle("--cui-primary"),
                        borderColor: "transparent",
                        borderWidth: 1,
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
          <CCol sm={4} md={3} xl={2}>
            <CWidgetStatsE
              chart={
                <CChartBar
                  className="mx-auto"
                  style={{ height: "40px", width: "80px" }}
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
                        backgroundColor: getStyle("--cui-success"),
                        borderColor: "transparent",
                        borderWidth: 1,
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
          <CCol sm={4} md={3} xl={2}>
            <CWidgetStatsE
              chart={
                <CChartLine
                  className="mx-auto"
                  style={{ height: "40px", width: "80px" }}
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
          <CCol sm={4} md={3} xl={2}>
            <CWidgetStatsE
              chart={
                <CChartLine
                  className="mx-auto"
                  style={{ height: "40px", width: "80px" }}
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
          <CCol sm={4} md={3} xl={2}>
            <CWidgetStatsE
              chart={
                <CChartLine
                  className="mx-auto"
                  style={{ height: "40px", width: "80px" }}
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
        </CRow>
      </CCardBody>
    </CCard>
  );
};
