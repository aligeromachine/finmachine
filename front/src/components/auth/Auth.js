import { useEffect } from 'react';
import { useDispatch } from 'react-redux';
import { protectedThunk } from '../../services/utils/token/state';
import { getAccessToken } from '../../utils/storage';

export const Auth = ({ children }) => {
    const dispatch = useDispatch();

    useEffect(() => {
        if (!getAccessToken()) dispatch(protectedThunk());
    }, [dispatch]);

    return children;
};
