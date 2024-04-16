import React, { useState } from "react"
import PieChart from "./components/PieChart"
import {Data} from "./utils/Data"
import { Link } from 'react-router-dom'

const Home = () => {
    // state for piechart
    const [userData, setUserData] = useState({
        // chartjs requires an object: [labels, datasets]
        // pull object from Data.js
        labels: Data.map((data)=>data.ticker),
        datasets: [{
            label: "Value",
            data: Data.map((data)=>data.value),
            borderWidth: 0,
            backgroundColor: [
                'rgba(48, 241, 183, 95)',
                'rgba(74, 201, 163, 97)',
                'rgba(84, 157, 135, 62)',
                'rgba(82, 117, 107, 46)',
                'rgba(63, 72, 69, 28)'
            ],
            hoverOffset: 24,
        }]
    })

    // button click handling function
    const handleClick = () => {
        console.log('test')
    }

    // parse data into separate vectors
    let valueData = Data.map((data)=>data.value);

    // add up a total portfolio value using Data.js
    let portfolioValue = 0;
    for (let i = 0; i < valueData.length; i++) {
        portfolioValue += valueData[i];
    }
    // add separating commas. EX: 3200 -> 3,200
    let portfolioValueString = portfolioValue.toLocaleString('en');

    return (
        <div className="content">
            <h2>Overview</h2>
            <div className="row">
                <div className="column">
                <div className="block">
                        <body>Portfolio Distribution</body>
                        <div className="chart">
                            <PieChart chartData={userData} />
                        </div>
                    </div>
                </div>
                <div className="column">
                    <div className="block">
                        <body>Portfolio Value</body>
                        <div className="box-content">
                            <h1 style={{
                                color: "#828196",
                                fontSize: "64px"
                            }}>$</h1>
                            <h1 style={{ fontSize: "64px" }}>
                                { portfolioValueString }
                            </h1>
                        </div>
                        <Link to="/new-stock">
                            <button className="button">
                                Add New Stock
                            </button>
                        </Link>    
                    </div>
                    <div className="block">
                        <body>Positions</body>
                        <div className="box-content" style={{display: "block"}}>
                            {Data.map((data) => (
                                <div className="position-preview" key={data.id}>
                                    <h3>{ data.ticker }</h3>
                                    <body className="value-preview">${ data.value } </body>
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