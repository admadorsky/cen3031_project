import { useState } from 'react'

const AddStockForm = ({ existingPosition = {}, updateCallback }) => {
    const [ticker, setTicker] = useState(existingPosition.ticker || "")
    const [quantity, setQuantity] = useState(existingPosition.quantity || 0)
    const [buyPrice, setBuyPrice] = useState(existingPosition.buyPrice || 0)
    const [isSold, setIsSold] = useState(existingPosition.isSold || 0)
    const [sellPrice, setSellPrice] = useState(existingPosition.sellPrice || 0)

    const updating = Object.entries(existingPosition).length !== 0

    const onSubmit = async (e) => {
        e.preventDefault()

        const data = {
            ticker,
            quantity,
            buyPrice,
            isSold,
            sellPrice
        }

        const url = "http://127.0.0.1:5000/" + (updating ? `update_position/${existingPosition.id}` : "create_position")
        const options = {
            method: updating ? "PATCH" : "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        }
        const response = await fetch(url, options)
        if (response.status !== 201 && response.status !== 200) {
            const data = await response.json()
            alert(data.message)
        } else {
            updateCallback()
        }
    }

    return (
        <div className="content">
            <form onSubmit={onSubmit}>
                <div>
                    <label htmlFor="ticker">Ticker:</label>
                    <input
                        type="text"
                        id="ticker"
                        value={ticker}
                        onChange={(e) => setTicker(e.target.value)}
                    />
                </div>
                <div>
                    <label htmlFor="quantity">Quantity:</label>
                    <input
                        type="number"
                        id="quantity"
                        value={quantity}
                        onChange={(e) => setQuantity(e.target.value)}
                    />
                </div>
                <div>
                    <label htmlFor="buyPrice">Price when bought:</label>
                    <input
                        type="number"
                        id="buyPrice"
                        value={buyPrice}
                        onChange={(e) => setBuyPrice(e.target.value)}
                    />
                </div>
                <div>
                    <label htmlFor="isSold">Is this stock sold?:</label>
                    <input
                        type="checkbox"
                        id="isSold"
                        value={isSold}
                        onChange={(e) => setIsSold(e.target.checked)}
                    />
                </div>
                <div>
                    <label htmlFor="sellPrice">Price when sold (leave blank if not sold):</label>
                    <input
                        type="number"
                        id="sellPrice"
                        value={sellPrice}
                        onChange={(e) => setSellPrice(e.target.value)}
                    />
                </div>
                <button type="submit" className='button' style={{float: "right"}}>
                    {updating ? "Submit" : "Add Stock"}
                </button>
            </form>
        </div>
    );
}
 
export default AddStockForm
{}