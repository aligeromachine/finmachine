import React, { useState } from "react";
import DatePicker from "react-datepicker";
import "./BigDatepicker.css"; // Файл со стилями из первого примера
import "react-datepicker/dist/react-datepicker.css";

const BigDatepicker = (props) => {
  return (
    <div className="big-datepicker-wrapper">
      <DatePicker {...props} wrapperClassName="big-datepicker" />
    </div>
  );
};

export const SimpleDatePicker = () => {
  const [startDate, setStartDate] = useState(new Date());

  return (
    <BigDatepicker
      selected={startDate}
      onChange={(date) => setStartDate(date)}
      dateFormat="dd.MM.yyyy"
      placeholderText="Выберите дату"
      isClearable
    />
  );
};

export const RangeDatePicker = () => {
  const [dateRange, setDateRange] = useState([null, null]);
  const [startDate, endDate] = dateRange;

  return (
    <BigDatepicker
      selectsRange
      startDate={startDate}
      endDate={endDate}
      onChange={(update) => setDateRange(update)}
      dateFormat="dd.MM.yyyy"
      placeholderText="Выберите период"
      isClearable
    />
  );
};
