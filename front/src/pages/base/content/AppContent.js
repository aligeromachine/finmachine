import React, { Suspense } from 'react';
import { Navigate, Route, Routes } from 'react-router-dom';
import { CContainer, CSpinner } from '@coreui/react';
import { contentRoutes } from './ContentRoutes.js';

function lazyImport(exportName) {
    return React.lazy(async () => {
        const module = await (() => import('../../index.js'))();
        return { default: module[exportName] };
    });
}

const Page404 = lazyImport('Page404');

export const AppContent = React.memo(() => {
    return (
        <CContainer className="px-4" fluid>
            <Suspense fallback={<CSpinner color="secondary" />}>
                <Routes>
                    {contentRoutes.map((route, idx) => {
                        return (
                            route.element && (
                                <Route key={idx} path={route.path} exact={route.exact} name={route.name} element={<route.element />} />
                            )
                        );
                    })}
                    <Route path="/" element={<Navigate to="dashboard" replace />} />
                    <Route path="*" name="Page 404" element={<Page404 />} />
                </Routes>
            </Suspense>
        </CContainer>
    );
});
