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

export const DatePicElem = ({ onChange, value, name }) => {
  const handleChange = (created) => {
    if (!created) return "";
    // Simulate standard input event
    const year = created.getFullYear();
    const month = String(created.getMonth() + 1).padStart(2, "0");
    const day = String(created.getDate()).padStart(2, "0");
    const hours = String(created.getHours()).padStart(2, "0");
    const minutes = String(created.getMinutes()).padStart(2, "0");
    const seconds = String(created.getSeconds()).padStart(2, "0");

    const syntheticEvent = {
      target: {
        name,
        value: `${year}-${month}-${day}T${hours}:${minutes}:${seconds}`,
      },
    };
    onChange(syntheticEvent);
  };
  return (
    <BigDatepicker
      selected={value}
      onChange={handleChange}
      dateFormat="dd-MM-yyyy"
      placeholderText="Выберите дату"
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
      timeFormat="HH:mm"
      dateFormat="dd-MM-yyyy"
      placeholderText="Выберите период"
      isClearable
    />
  );
};
