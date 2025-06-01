import React, { Suspense } from "react";
import { HashRouter, Route, Routes } from "react-router-dom";
import { CSpinner } from "@coreui/react";
import { GuestGuard, AuthGuard } from "./components/auth/Protect";

import "./scss/style.scss";
import "./scss/examples.scss";

function lazyImport(exportName) {
  return React.lazy(async () => {
    const module = await (() => import("./pages/"))();
    return { default: module[exportName] };
  });
}

const Layout = lazyImport("Layout");
const Login = lazyImport("Login");
const Register = lazyImport("Register");
const Page404 = lazyImport("Page404");
const Page500 = lazyImport("Page500");

const App = () => {
  return (
    <HashRouter>
      <Suspense
        fallback={
          <div className="pt-3 text-center">
            <CSpinner color="primary" variant="grow" />
          </div>
        }
      >
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
            element={<AuthGuard inner={<Layout />} />}
          />
        </Routes>
      </Suspense>
    </HashRouter>
  );
};

export default App;
