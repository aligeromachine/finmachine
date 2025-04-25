import React, { Suspense, useEffect } from "react";
import { HashRouter, Route, Routes } from "react-router-dom";
import { useSelector } from "react-redux";
import { CSpinner, useColorModes } from "@coreui/react";
import { GuestGuard, AuthGuard } from "./components/auth/Protect";
import { Token } from "./components/auth/Token";
import "./scss/style.scss";

// We use those styles to show code examples, you should remove them in your application.
import "./scss/examples.scss";

// Containers
const DefaultLayout = React.lazy(() => import("./layout/DefaultLayout"));

// Pages
const Login = React.lazy(() => import("./pages/login/Login"));
const Register = React.lazy(() => import("./pages/register/Register"));
const Page404 = React.lazy(() => import("./pages/page404/Page404"));
const Page500 = React.lazy(() => import("./pages/page500/Page500"));

const App = () => {
  const { isColorModeSet, setColorMode } = useColorModes(
    "coreui-free-react-admin-template-theme",
  );
  const storedTheme = useSelector((state) => state.theme);

  useEffect(() => {
    const urlParams = new URLSearchParams(window.location.href.split("?")[1]);
    const theme =
      urlParams.get("theme") &&
      urlParams.get("theme").match(/^[A-Za-z0-9\s]+/)[0];
    if (theme) {
      setColorMode(theme);
    }

    if (isColorModeSet()) {
      return;
    }

    setColorMode(storedTheme);
  }, []); // eslint-disable-line react-hooks/exhaustive-deps

  return (
    <HashRouter>
      <Suspense
        fallback={
          <div className="pt-3 text-center">
            <CSpinner color="primary" variant="grow" />
          </div>
        }
      >
        <Token />
        <Routes>
          <Route
            exact
            path="/login"
            name="Login Page"
            element={<GuestGuard inner={<Login />} />}
          />
          <Route
            exact
            path="/register"
            name="Register Page"
            element={<GuestGuard inner={<Register />} />}
          />
          <Route
            exact
            path="/404"
            name="Page 404"
            element={<GuestGuard inner={<Page404 />} />}
          />
          <Route
            exact
            path="/500"
            name="Page 500"
            element={<GuestGuard inner={<Page500 />} />}
          />
          <Route
            path="*"
            name="Home"
            element={<AuthGuard inner={<DefaultLayout />} />}
          />
        </Routes>
      </Suspense>
    </HashRouter>
  );
};

export default App;
