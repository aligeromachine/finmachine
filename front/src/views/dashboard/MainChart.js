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
import Chart from "react-apexcharts";

const LineChart = () => {
  const options = {
    chart: {
      id: "styled-chart",
      foreColor: " #3553",
      toolbar: {
        show: false,
      },
    },
    colors: ["#008FFB", "#00E396", "#FEB019", "#FF4560", "#775DD0"],
    theme: {
      mode: "light", // or 'dark'
      palette: "palette1", // palette1 to palette10
    },
    stroke: {
      curve: "smooth",
      width: 3,
    },
    xaxis: {
      categories: [
        1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001,
      ],
    },
  };

  const series = [
    {
      name: "series-1",
      data: [30, 40, 45, 50, 49, 60, 70, 91, 34, 45, 67],
    },
  ];

  return (
    <div className="app">
      <div className="row">
        <div className="mixed-chart">
          <Chart
            options={options}
            series={series}
            type="line"
            width="100%"
            height="700"
          />
        </div>
      </div>
    </div>
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
              Статистика
            </h4>
          </CCol>
        </CRow>
        <LineChart />
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
