const PositionsList = ({positions, updatePosition, updateCallback}) => {

    const onDelete = async (id) => {
        try {
            const options = {
                method: "DELETE"
            }
            const response = await fetch(`http://127.0.0.1:5000/delete_position/${id}`, options)

            if (response.status === 200) {
                updateCallback()
            } else {
                console.error("Failed to delete")
            }
        } catch (error) {
            alert(error)
        }
    }

    return (
        <div className="content">
            <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" />
            <h2>Positions</h2>
            <div className="block">
                <table width="100%">
                    <thead>
                        <tr>
                            <th>Ticker</th>
                            <th>Quantity</th>
                            <th>Price When Bought</th>
                            <th>Total Gain/Loss</th>
                            <th>Actions</th>
                        </tr>
                    </thead>
                    <tbody>
                        {positions.map((position) => (
                            <tr key={position.id} className={position.isSold === "1" ? "sold" : "market"}>
                                <td>{position.ticker}</td>
                                <td>{position.quantity}</td>
                                <td>${position.buyPrice}</td>
                                <td>${(((position.sellPrice)*(position.quantity))-((position.buyPrice)*(position.quantity))).toFixed(2)}{position.isSold === "1" ? " (sold)" : ""}</td>
                                <td className="tbutton-container">
                                    <button className="tbutton" onClick={() => updatePosition(position)}>
                                        <span className="material-symbols-outlined">edit</span>
                                    </button>
                                    <button className="tbutton red" onClick={() => onDelete(position.id)}>
                                        <span className="material-symbols-outlined">delete</span>
                                    </button>
                                </td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
        </div>
    );
}
 
export default PositionsList;