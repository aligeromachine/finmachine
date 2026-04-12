import { useState } from 'react';
import { useDispatch } from 'react-redux';

export const UseTable = () => {
    const dispatch = useDispatch();

    const onSet = (func, value) => {
        dispatch(func({ [value]: value }));
    };

    return { onSet };
};
