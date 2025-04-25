import React from "react";
import { useSelector, useDispatch } from "react-redux";

import {
  CCloseButton,
  CSidebar,
  CSidebarFooter,
  CSidebarHeader,
  CSidebarToggler,
  CSidebarBrand,
} from "@coreui/react";

import { AppSidebarNav } from "./AppSidebarNav";
import { changeSideShow, changeSideUnfo } from "../services/stateBar";

// sidebar nav config
import navigation from "../_nav";

import imageIco from "../assets/brand/chart.png";

const AppSidebar = () => {
  const dispatch = useDispatch();
  const { sidebarShow, sidebarUnfoldable } = useSelector(
    (state) => state.barReducer,
  );

  return (
    <CSidebar
      className="border-end"
      colorScheme="dark"
      position="fixed"
      unfoldable={sidebarUnfoldable}
      visible={sidebarShow}
      onVisibleChange={(visible) => {
        dispatch(changeSideShow(visible));
      }}
    >
      <CSidebarHeader className="border-bottom">
        <CSidebarBrand to="/">
          <img src={imageIco} height={24} width={24} />
        </CSidebarBrand>
        <CCloseButton
          className="d-lg-none"
          dark
          onClick={() => dispatch(changeSideShow(false))}
        />
      </CSidebarHeader>
      <AppSidebarNav items={navigation} />
      <CSidebarFooter className="border-top d-none d-lg-flex">
        <CSidebarToggler
          onClick={() => dispatch(changeSideUnfo(!sidebarUnfoldable))}
        />
      </CSidebarFooter>
    </CSidebar>
  );
};

export default React.memo(AppSidebar);
