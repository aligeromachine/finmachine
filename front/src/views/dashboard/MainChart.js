import React, { useEffect, useRef } from "react";
import { CChartLine } from "@coreui/react-chartjs";
import { getStyle } from "@coreui/utils";
import classNames from "classnames";
import {
  CAvatar,
  CButton,
  CButtonGroup,
  CCard,
  CCardBody,
  CCardFooter,
  CCol,
  CProgress,
  CRow,
} from "@coreui/react";
import CIcon from "@coreui/icons-react";
import { cilCloudDownload } from "@coreui/icons";

const MainChart = () => {
  const chartRef = useRef(null);

  useEffect(() => {
    document.documentElement.addEventListener("ColorSchemeChange", () => {
      if (chartRef.current) {
        setTimeout(() => {
          chartRef.current.options.scales.x.grid.borderColor = getStyle(
            "--cui-border-color-translucent",
          );
          chartRef.current.options.scales.x.grid.color = getStyle(
            "--cui-border-color-translucent",
          );
          chartRef.current.options.scales.x.ticks.color =
            getStyle("--cui-body-color");
          chartRef.current.options.scales.y.grid.borderColor = getStyle(
            "--cui-border-color-translucent",
          );
          chartRef.current.options.scales.y.grid.color = getStyle(
            "--cui-border-color-translucent",
          );
          chartRef.current.options.scales.y.ticks.color =
            getStyle("--cui-body-color");
          chartRef.current.update();
        });
      }
    });
  }, [chartRef]);

  const random = () => Math.round(Math.random() * 100);

  return (
    <>
      <CChartLine
        ref={chartRef}
        style={{ height: "300px", marginTop: "40px" }}
        data={{
          labels: [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
          ],
          datasets: [
            {
              label: "My First dataset",
              backgroundColor: `rgba(${getStyle("--cui-info-rgb")}, .1)`,
              borderColor: getStyle("--cui-info"),
              pointHoverBackgroundColor: getStyle("--cui-info"),
              borderWidth: 2,
              data: [
                random(50, 200),
                random(50, 200),
                random(50, 200),
                random(50, 200),
                random(50, 200),
                random(50, 200),
                random(50, 200),
              ],
              fill: true,
            },
            {
              label: "My Second dataset",
              backgroundColor: "transparent",
              borderColor: getStyle("--cui-success"),
              pointHoverBackgroundColor: getStyle("--cui-success"),
              borderWidth: 2,
              data: [
                random(50, 200),
                random(50, 200),
                random(50, 200),
                random(50, 200),
                random(50, 200),
                random(50, 200),
                random(50, 200),
              ],
            },
            {
              label: "My Third dataset",
              backgroundColor: "transparent",
              borderColor: getStyle("--cui-danger"),
              pointHoverBackgroundColor: getStyle("--cui-danger"),
              borderWidth: 1,
              borderDash: [8, 5],
              data: [65, 65, 65, 65, 65, 65, 65],
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
              grid: {
                color: getStyle("--cui-border-color-translucent"),
                drawOnChartArea: false,
              },
              ticks: {
                color: getStyle("--cui-body-color"),
              },
            },
            y: {
              beginAtZero: true,
              border: {
                color: getStyle("--cui-border-color-translucent"),
              },
              grid: {
                color: getStyle("--cui-border-color-translucent"),
              },
              max: 250,
              ticks: {
                color: getStyle("--cui-body-color"),
                maxTicksLimit: 5,
                stepSize: Math.ceil(250 / 5),
              },
            },
          },
          elements: {
            line: {
              tension: 0.4,
            },
            point: {
              radius: 0,
              hitRadius: 10,
              hoverRadius: 4,
              hoverBorderWidth: 3,
            },
          },
        }}
      />
    </>
  );
};

export const BaseChart = () => {
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
    <CCard className="mb-4">
      <CCardBody>
        <CRow>
          <CCol sm={5}>
            <h4 id="traffic" className="card-title mb-0">
              Traffic
            </h4>
            <div className="small text-body-secondary">January - July 2023</div>
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
  );
};
