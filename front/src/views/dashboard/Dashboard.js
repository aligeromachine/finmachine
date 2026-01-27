import { useState, useEffect } from "react";
import { Auth } from "../../components/auth/Auth";
import { WdChart } from "./WdChart";
import { WdProfit } from "./WdProfit";
import { WdStat } from "./WdStat";
import { WdBuy } from "./WdBuy";
import { getDash } from "../../services/dash/query";

export const Dashboard = () => {
  const [data, setData] = useState({});
  useEffect(() => {
    const fetchOptions = async () => {
      const response = await getDash();
      if (response) setData(response);
    };
    fetchOptions();
  }, []);

  return (
    <Auth>
      <WdStat data={data.capital} card={data.cards} />
      <WdProfit data={data.profit} />
      <WdBuy data={data.buy} daily={data.daily} shop={data.shop} />
      <WdChart />
    </Auth>
  );
};
