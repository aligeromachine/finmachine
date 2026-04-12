import React, { Suspense } from 'react';
import { HashRouter, Route, Routes } from 'react-router-dom';
import { CSpinner } from '@coreui/react';
import { Authenticated, Unauthorized } from '../components/auth/Protect.js';

import '../scss/style.scss';
import '../scss/examples.scss';
import '../scss/JsonTextarea.css';

function lazyImport(exportName) {
    return React.lazy(async () => {
        const module = await (() => import('./index.js'))();
        return { default: module[exportName] };
    });
}

const Base = lazyImport('Base');
const Login = lazyImport('Login');
const Register = lazyImport('Register');
const Page404 = lazyImport('Page404');
const Page500 = lazyImport('Page500');

export const PageConstructor = () => {
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
                    <Route exact path="/login" name="Login Page" element={<Unauthorized inner={<Login />} />} />
                    <Route exact path="/register" name="Register Page" element={<Unauthorized inner={<Register />} />} />
                    <Route exact path="/404" name="Page 404" element={<Unauthorized inner={<Page404 />} />} />
                    <Route exact path="/500" name="Page 500" element={<Unauthorized inner={<Page500 />} />} />
                    <Route path="*" name="Home" element={<Authenticated inner={<Base />} />} />
                </Routes>
            </Suspense>
        </HashRouter>
    );
};
