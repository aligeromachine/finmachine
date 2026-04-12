import React, { useState, useEffect } from 'react';
import Select from 'react-select';

export const SelectElem = ({ options, value, onChange, name, placeholder }) => {
    const [selected, setSelected] = useState(value || []);
    const handleChange = invouter => {
        const syntheticEvent = {
            target: {
                name: name,
                value: invouter,
            },
        };
        setSelected(invouter);
        onChange(syntheticEvent);
    };
    useEffect(() => {
        setSelected(value || []);
    }, [value]);
    return (
        <Select
            options={options}
            value={selected}
            onChange={handleChange}
            name={name}
            placeholder={placeholder}
            isMulti
            className="basic-multi-select"
            classNamePrefix="select"
        />
    );
};
