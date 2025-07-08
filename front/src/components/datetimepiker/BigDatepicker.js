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
    // Simulate standard input event
    const syntheticEvent = {
      target: {
        name: "created", // or whatever name you need
        value: String(created).split("GMT")[0].trim(),
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
      name={name}
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
