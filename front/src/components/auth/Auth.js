import { useEffect } from 'react';
import { useDispatch } from 'react-redux';
import { refreshThunk } from '../../services/token/state';
import { getAccessToken } from '../../utils/storage';

export const Auth = ({ children }) => {
    const dispatch = useDispatch();

    useEffect(() => {
        if (!getAccessToken()) dispatch(refreshThunk());
    }, [dispatch]);

    return children;
};
