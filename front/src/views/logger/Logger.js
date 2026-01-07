import { useState, useEffect } from "react";
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
import { ButtonBase } from "../../components/elems/Button";
import { Auth } from "../../components/auth/Auth";
import { getLogger, delLogger } from "../../services/logger/query";
import { MONEY, DJANGO, API } from "../../services/logger/const";
import { CodeBlock } from "../../components/elems/CodeBlock";
import { handleDeleteLog } from "../../components/action/Action";

export const Logger = () => {
  const [dataLog, setLog] = useState({});
  useEffect(() => {
    const fetchOptions = async () => {
      const data = await getLogger();

      if (data) {
        setLog(data.message);
      }
    };

    fetchOptions();
  }, []);

  const baseClick = async (msg) => {
    const freeCanvas = async () => {
      const data = await delLogger(msg);
      setLog({ ...dataLog, ...{ [msg]: data.message } });
    };
    handleDeleteLog(msg, freeCanvas);
  };

  return (
    <Auth>
      <CRow>
        <CCol xs={12}>
          <CCard className="mb-4">
            <CCardHeader>
              <strong>Logger</strong>
            </CCardHeader>
            <CCardBody>

              <CTabs defaultActiveItemKey="money">
                <CTabList variant="tabs">
                  <CTab itemKey="money">Money</CTab>
                  <CTab itemKey="api">Api</CTab>
                  <CTab itemKey="django">Django</CTab>

                </CTabList>
                <CTabContent>
                  <CTabPanel className="p-3" itemKey="money">
                    <ButtonBase
                      title={"Clear"}
                      onClick={() => {
                        baseClick(MONEY);
                      }}
                    />
                    <CodeBlock content={dataLog.money} />
                  </CTabPanel>
                  <CTabPanel className="p-3" itemKey="api">
                    <ButtonBase
                      title={"Clear"}
                      onClick={() => {
                        baseClick(API);
                      }}
                    />
                    <CodeBlock content={dataLog.api} />
                  </CTabPanel>
                  <CTabPanel className="p-3" itemKey="django">
                    <ButtonBase
                      title={"Clear"}
                      onClick={() => {
                        baseClick(DJANGO);
                      }}
                    />
                    <CodeBlock content={dataLog.django} />
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
