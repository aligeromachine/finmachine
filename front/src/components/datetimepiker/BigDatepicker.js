import React, { useState, useEffect } from 'react';
import DatePicker from 'react-datepicker';
import './BigDatepicker.css'; // Файл со стилями из первого примера
import 'react-datepicker/dist/react-datepicker.css';

export const timeF = created => {
    if (!created) return '';
    if (created instanceof Date) {
        const year = created.getFullYear();
        const month = created.getMonth();
        const day = String(created.getDate()).padStart(2, '0');
        const hours = String(created.getHours()).padStart(2, '0');
        const minutes = String(created.getMinutes()).padStart(2, '0');
        const seconds = String(created.getSeconds()).padStart(2, '0');
        return new Date(year, month, day, hours, minutes, seconds);
    } else {
        const regex = /(\d{2})-(\d{2})-(\d{4}) (\d{2}):(\d{2}):(\d{2})/;
        const raw = String(created).match(regex);
        if (!raw) {
            return new Date();
        }
        const [, day, month, year, hours, minutes, seconds] = raw;
        return new Date(year, month, day, hours, minutes, seconds);
    }
};

const BigDatepicker = props => {
    return (
        <div className="big-datepicker-wrapper">
            <DatePicker {...props} wrapperClassName="big-datepicker" />
        </div>
    );
};

export const DatePicElem = ({ onChange, value, name }) => {
    const handleChange = created => {
        if (!created) return '';
        const syntheticEvent = {
            target: {
                name,
                value: timeF(created),
            },
        };
        onChange(syntheticEvent);
    };
    useEffect(() => {
        if (!value) {
            handleChange(new Date());
        }
    }, [value]);
    return <BigDatepicker selected={value} onChange={handleChange} dateFormat="dd-MM-yyyy" placeholderText="Выберите дату" />;
};

export const RangeDatePicker = () => {
    const [dateRange, setDateRange] = useState([null, null]);
    const [startDate, endDate] = dateRange;

    return (
        <BigDatepicker
            selectsRange
            startDate={startDate}
            endDate={endDate}
            onChange={update => setDateRange(update)}
            timeFormat="HH:mm"
            dateFormat="dd-MM-yyyy"
            placeholderText="Выберите период"
            isClearable
        />
    );
};
