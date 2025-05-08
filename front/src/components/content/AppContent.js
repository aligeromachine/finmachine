import React, { Suspense } from "react";
import { Navigate, Route, Routes } from "react-router-dom";
import { CContainer, CSpinner } from "@coreui/react";
import { routes } from "./routes";

const Page404 = React.lazy(() => import("../../pages/page404/Page404"));

const AppContent = () => {
  return (
    <CContainer className="px-4" fluid>
      <Suspense fallback={<CSpinner color="secondary" />}>
        <Routes>
          {routes.map((route, idx) => {
            return (
              route.element && (
                <Route
                  key={idx}
                  path={route.path}
                  exact={route.exact}
                  name={route.name}
                  element={<route.element />}
                />
              )
            );
          })}
          <Route path="/" element={<Navigate to="dashboard" replace />} />
          <Route path="*" name="Page 404" element={<Page404 />} />
        </Routes>
      </Suspense>
    </CContainer>
  );
};

export default React.memo(AppContent);
