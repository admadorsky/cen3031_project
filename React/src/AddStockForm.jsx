import { useState } from 'react'

const AddStockForm = ({updateCallback}) => {
    const [ticker, setTicker] = useState("")
    const [quantity, setQuantity] = useState()
    const [buyPrice, setBuyPrice] = useState()
    const [isSold, setIsSold] = useState("")
    const [sellPrice, setSellPrice] = useState()

    const onSubmit = async (e) => {
        e.preventDefault()

        const data = {
            ticker,
            quantity,
            buyPrice,
            isSold,
            sellPrice
        }

        const url = "http://127.0.0.1:5000/create_position"
        const options = {
            method: "POST",
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
            // success
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
                        onChange={(e) => setIsSold(e.target.value)}
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
                    Add Stock
                </button>
            </form>
        </div>
    );
}
 
export default AddStockForm
{}