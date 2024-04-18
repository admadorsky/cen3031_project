import React, { useState, useEffect } from "react"
import PieChart from "./components/PieChart"
import { Link } from 'react-router-dom'

const Home = () => {

    const [positions, setPositions] = useState([])

    useEffect(() => {
        fetchPositions()
    }, [])

    const fetchPositions = async () => {
        const response = await fetch("http://127.0.0.1:5000/portfolio");
        const fetchData = await response.json();
        setPositions(fetchData.positions);
      };

    // button click handling function
    const handleClick = () => {
        console.log('test')
    }

    // add up a total portfolio value using database
    let portfolioValue = 0;
    let portfolioInvestment = 0;
    for (let i = 0; i < positions.length; i++) {
        portfolioValue += (positions[i].sellPrice * positions[i].quantity);
        portfolioInvestment += (positions[i].buyPrice * positions[i].quantity);
    }

    let portfolioGainLoss = portfolioValue - portfolioInvestment;

    // add separating commas. EX: 3200 -> 3,200
    // portfolioValue = portfolioValue.toFixed(2)
    // portfolioGainLoss = portfolioGainLoss.toFixed(2)
    let portfolioValueString = portfolioValue.toLocaleString("en-US", {style:"currency", currency:"USD"});
    let portfolioGainLossString = portfolioGainLoss.toLocaleString("en-US", {style:"currency", currency:"USD"});

    return (
        <div className="content">
            <h2>Overview</h2>
            <div className="row">
                <div className="column">
                <div className="block">
                        <p>Portfolio Distribution</p>
                        <div className="chart">
                            <PieChart chartData={{
                                labels: positions.map((data) => (data.ticker)),
                                datasets: [
                                {
                                    label: "Value",
                                    data: positions.map((data)=>(data.sellPrice*data.quantity)),
                                    borderWidth: 0,
                                    hoverOffset: 24,
                                    backgroundColor: [
                                        'rgba(48, 241, 183, 95)',
                                        'rgba(74, 201, 163, 97)',
                                        'rgba(84, 157, 135, 62)',
                                        'rgba(82, 117, 107, 46)',
                                        'rgba(63, 72, 69, 28)'
                                    ]
                                }
                                ]
                            }} />
                        </div>
                    </div>
                </div>
                <div className="column">
                    <div className="block">
                        <p>Portfolio Value</p>
                        <div className="box-content">
                            <h1 style={{ fontSize: "64px" }}>
                                { portfolioValueString }
                            </h1>
                        </div>
                        <p>Total Gain/Loss: {portfolioGainLossString}</p> 
                    </div>
                    <div className="block">
                        <p>Positions</p>
                        <div className="box-content" style={{display: "block"}}>
                            {positions.map((data) => (
                                <div className="position-preview" key={data.id}>
                                    <h3>{ data.ticker }</h3>
                                    <p className="value-preview">${ (data.sellPrice * data.quantity).toFixed(2) } </p>
                                </div>
                            ))}
                        </div>
                        <Link to="/portfolio">
                            <button className="button">
                                Manage Stocks
                            </button>
                        </Link>
                    </div>
                </div>
            </div>
        </div>
    );
}
 
export default Home;