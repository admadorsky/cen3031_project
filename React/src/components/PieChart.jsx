import 'chart.js/auto'
import { Doughnut } from "react-chartjs-2"

function PieChart({chartData}) {
    return <Doughnut data={chartData}></Doughnut>
}
 
export default PieChart;