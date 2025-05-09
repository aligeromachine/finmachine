import React from "react";
import {
  AppContent,
  AppSidebar,
  AppFooter,
  AppHeader,
} from "../../components/content/index";

export const Layout = () => {
  return (
    <div>
      <AppSidebar />
      <div className="wrapper d-flex flex-column min-vh-100">
        <AppHeader />
        <div className="body flex-grow-1">
          <AppContent />
        </div>
        <AppFooter />
      </div>
    </div>
  );
};
