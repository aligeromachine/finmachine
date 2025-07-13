import { useState, useEffect } from "react";
import { Auth } from "../../components/auth/Auth";
import { WidgetChart } from "./WidgetChart";
import { BaseChart } from "./MainChart";
import { WidgetSolid } from "./WidgetSolid";
import { WidgetBase } from "./WidgetBase";
import { WidgetSim } from "./WidgetSim";
import { getDash } from "../../services/dash/query";

export const Dashboard = () => {
  const [dataDs, setDataDs] = useState({});
  useEffect(() => {
    const fetchOptions = async () => {
      const data = await getDash();
      if (data) {
        setDataDs(data);
      }
    };

    fetchOptions();
  }, []);

  return (
    <Auth>
      <WidgetSolid data={dataDs} />
      <WidgetBase data={dataDs} />
      <WidgetSim data={dataDs} />
      <BaseChart />
    </Auth>
  );
};
