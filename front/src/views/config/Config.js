import {
  CCard,
  CCardBody,
  CCol,
  CRow,
  CTab,
  CTabContent,
  CTabList,
  CTabPanel,
  CTabs,
  CCardHeader,
} from "@coreui/react";
import { ModalProvider } from "../../components/hook/ModalContext";
import { Header } from "../../components/elems/Header";
import { Button } from "../../components/elems/Button";
import { Auth } from "../../components/auth/Auth";

import "../../libs/prism-coy.css";

export const Config = () => {
  return (
    <Auth>
      <CRow>
        <CCol xs={12}>
          <CCard className="mb-4">
            <CCardHeader>
              <strong>Logger</strong>
            </CCardHeader>
            <CCardBody>
              <CTabs defaultActiveItemKey="home-tab-pane">
                <CTabList variant="underline-border">
                  <CTab itemKey="home-tab-pane">
                    Money
                  </CTab>
                  <CTab itemKey="profile-tab-pane">
                    Api
                  </CTab>
                  <CTab itemKey="contact-tab-pane">
                    Django
                  </CTab>
                </CTabList>
                <CTabContent>
                  <CTabPanel
                    className="py-3"
                    itemKey="home-tab-pane"
                  >
                    <CCardBody>
                      <code className="language-makrup">
                        classes are also available, for when you want to match
                        the font styling of a heading but cannot use the
                        associated HTML element.classes are also available, for
                        when you want to match the font styling of a heading but
                        cannot use the associated HTML element.classes are also
                        available, for when you want to match the font styling
                        of a heading but cannot use the associated HTML
                        element.classes are also available, for when you want to
                        match the font styling of a heading but cannot use the
                        associated HTML element.classes are also available, for
                        when you want to match the font styling of a heading but
                        cannot use the associated HTML element.classes are also
                        available, for when you want to match the font styling
                        of a heading but cannot use the associated HTML
                        element.classes are also available, for when you want to
                        match the font styling of a heading but cannot use the
                        associated HTML element.classes are also available, for
                        when you want to match the font styling of a heading but
                        cannot use the associated HTML element.classes are also
                        available, for when you want to match the font styling
                        of a heading but cannot use the associated HTML
                        element.classes are also available, for when you want to
                        match the font styling of a heading but cannot use the
                        associated HTML element.classes are also available, for
                        when you want to match the font styling of a heading but
                        cannot use the associated HTML element.classes are also
                        available, for when you want to match the font styling
                        of a heading but cannot use the associated HTML
                        element.classes are also available, for when you want to
                        match the font styling of a heading but cannot use the
                        associated HTML element.classes are also available, for
                        when you want to match the font styling of a heading but
                        cannot use the associated HTML element.classes are also
                        available, for when you want to match the font styling
                        of a heading but cannot use the associated HTML element.
                      </code>
                    </CCardBody>
                  </CTabPanel>
                  <CTabPanel
                    className="py-3"
                    itemKey="profile-tab-pane"
                  >
                    Profile tab content
                  </CTabPanel>
                  <CTabPanel
                    className="py-3"
                    itemKey="contact-tab-pane"
                  >
                    Contact tab content
                  </CTabPanel>
                </CTabContent>
              </CTabs>
            </CCardBody>
          </CCard>
        </CCol>
      </CRow>
    </Auth>
  );
};
