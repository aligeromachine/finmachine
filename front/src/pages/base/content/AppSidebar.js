import React from 'react';
import { useSelector, useDispatch } from 'react-redux';

import { CCloseButton, CSidebar, CSidebarFooter, CSidebarHeader, CSidebarToggler, CSidebarBrand } from '@coreui/react';

import { AppSidebarNav } from './AppSidebarNav';
import { contentItems } from './contentItems';

import { changeSideShow, changeSideUnfo } from '../../../services/utils/bar/state';
import imageIco from '../../../assets/brand/chart.png';
import { getVersion } from '../../../services/utils/bar/query';

export const AppSidebar = React.memo(() => {
    const dispatch = useDispatch();
    const { sidebarShow, sidebarUnfoldable } = useSelector(state => state.barReducer);

    const [version, setVersion] = React.useState('0.0.0');
    React.useEffect(() => {
        const fetchOptions = async () => {
            const response = await getVersion();
            if (response) setVersion(response.version);
        };
        fetchOptions();
    }, []);

    return (
        <CSidebar
            className="border-end"
            colorScheme="dark"
            position="fixed"
            unfoldable={sidebarUnfoldable}
            visible={sidebarShow}
            onVisibleChange={visible => {
                dispatch(changeSideShow(visible));
            }}
        >
            <CSidebarHeader className="border-bottom">
                <CSidebarBrand to="/">
                    <img src={imageIco} height={32} width={32} />
                </CSidebarBrand>
                <h5>{version}</h5>
                <CCloseButton className="d-lg-none" dark onClick={() => dispatch(changeSideShow(false))} />
            </CSidebarHeader>
            <AppSidebarNav items={contentItems} />
            <CSidebarFooter className="border-top d-none d-lg-flex">
                <CSidebarToggler onClick={() => dispatch(changeSideUnfo(!sidebarUnfoldable))} />
            </CSidebarFooter>
        </CSidebar>
    );
});
